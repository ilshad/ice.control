### -*- coding: utf-8 -*- ####################################################
#
#  Copyright (C) 2010 Ilshad R. Khabibullin <astoon.net at gmail.com>
#
#  This library is free software: you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License.
#
#  This library is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#  or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
#  for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from zope.interface import implements, Interface
from zope.component import adapts, queryMultiAdapter
from zope.dublincore.interfaces import IZopeDublinCore
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.interface.common.mapping import IEnumerableMapping
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.container.interfaces import IReadContainer
from zope.location.interfaces import ILocationInfo
from zope.size.interfaces import ISized
from interfaces import IXML, ICON_ADAPTER_NAME
from lexeme import *

class XMLBase(object):
    implements(IXML)
    adapts(Interface, IBrowserRequest)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def name(self):
        # This method is filter
        try:
            return NAME % ILocationInfo(self.context).getName()
        except TypeError:
            return None

    def url(self):
        # This method is common and it needn't to be reimplement
        # in subclasses in standard situations.
        return URL % absoluteURL(self.context, self.request)

    def title(self):
        # Sometimes you need to reimplement this method in subclass,
        # mostly if an object does not uses Dublin Core metadata
        try:
            dc = IZopeDublinCore(self.context)
            return dc.title and TITLE % dc.title or u''
        except TypeError:
            return u''

    def icon_url(self):
        # This method needn't to reimplement never. Define icon for
        # new content type using special zcml directive
        icon = queryMultiAdapter(
            (self.context, self.request), name=ICON_ADAPTER_NAME)
        if icon:
            return ICON_URL % icon.url()
        return u''

    def size(self):
        # This is common pattern. If you have defined adapter to ISized
        # then you needn't to reimplement this method in subclasses.
        try:
            return SIZE % ISized(self.context).sizeForDisplay()
        except TypeError:
            return u''

    def is_container(self):
        # I recommend reimplement this and return IS_CONTAINER
        # or empty string directly
        if IReadContainer.providedBy(self.context):
            return IS_CONTAINER
        return u''

    def length(self):
        # I strongly recommend to reimplement this in your subclass
        try:
            enumerable = IEnumerableMapping(self.context)
        except TypeError:
            return u''
        return LENGTH % len(enumerable)

    def sort_key(self):
        # Reimplement if you like sort this item within its
        # parent container
        return None

    def children(self):
        # If you need custom filter then reimplement this method.
        # Otherwise this implementation is generic and it is correct
        # for standard cases.
        try:
            rc = IReadContainer(self.context)
        except TypeError:
            return u''
        specs = []
        for v in rc.values():
            spec = queryMultiAdapter((v, self.request), IXML)
            if spec:
                specs.append(spec)
        specs.sort(key = lambda x: x.sort_key())
        lexemes = [CHILD % x.xml_lexemes() for x in specs]
        return CHILDREN % u'\n'.join(lexemes)

    def xml_lexemes(self):
        # This method is common and needn't to be reimplemented in subclasses
        if self.name() is not None:
            return self.name() + self.url() + self.title() + \
                self.icon_url() + self.size() + self.is_container() + \
                self.length()
        return u''

    def xml_document(self):
        # This method is common and needn't to be reimplemented in subclasses
        return XML_HEAD + XML_ROOT % (THIS % self.xml_lexemes() + u'\n' + self.children())
