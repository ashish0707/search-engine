import abc


class SimilarityMeasure(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def rank_and_store_documents(self, query,querynumber):
        """ranks and store the documents"""
        return



