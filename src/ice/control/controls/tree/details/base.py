# coding: utf-8

from zope.dublincore.interfaces import IZopeDublinCore

class DetailsBase:

    def getTitle(self):
        dc = IZopeDublinCore(self.context, None)
        return dc and dc.title

