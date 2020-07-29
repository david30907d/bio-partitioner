"""
Use this factory to create partitioner
"""
from biopartitioner.partitioner.vcf_partitioner import VCFPartitioner


class PartitionerFactory:
    """
    facotry object
    """

    @classmethod
    def create_partitioner(cls, type_of_dataset):
        """
        main function
        """
        if type_of_dataset == "vcf":
            return VCFPartitioner
        raise Exception("Invalid partitioner")
