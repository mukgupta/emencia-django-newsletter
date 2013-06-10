"""Utils for newsletter"""
from BeautifulSoup import BeautifulSoup
from django.core.urlresolvers import reverse

from emencia.django.newsletter.models import Link
from emencia.django.newsletter.settings import USE_PRETTIFY


def body_insertion(content, insertion, end=False):
    """Insert an HTML content into the body HTML node"""
    insertion = BeautifulSoup(insertion)
    soup = BeautifulSoup(content)

    if soup.body and end:
        soup.body.append(insertion)
    elif soup.body:
        soup.body.insert(0, insertion)
    elif not soup.body and end:
        soup.append(insertion)
    elif not soup.body:
        soup.insert(0, insertion)

    if USE_PRETTIFY:
        return soup.prettify()
    else:
        return soup.renderContents()


def additional_insertion(content, insertion):
    """insert additional content into <div id="additional-content"></div>"""
    insertion = BeautifulSoup(insertion)
    soup = BeautifulSoup(content)

    if soup('div', id='additional-content'):
        soup('div', id='additional-content')[0].contents[0].replaceWith(insertion)

    if USE_PRETTIFY:
        return soup.prettify()
    else:
        return soup.renderContents()


def track_links(content, context):
    """Convert all links in the template for the user
    to track his navigation"""
    if not context.get('uidb36'):
        return content

    soup = BeautifulSoup(content)
    for link_markup in soup('a'):
        if link_markup.get('href') and \
               'no-track' not in link_markup.get('rel', ''):
            link_href = link_markup['href']
            link_title = link_markup.get('title', link_href)
            link, created = Link.objects.get_or_create(url=link_href,
                                                       defaults={'title': link_title})
            link_markup['href'] = 'http://%s%s' % (context['domain'], reverse('newsletter_newsletter_tracking_link',
                                                                              args=[context['newsletter'].slug,
                                                                                    context['uidb36'], context['token'],
                                                                                    link.pk]))
    if USE_PRETTIFY:
        return soup.prettify()
    else:
        return soup.renderContents()
