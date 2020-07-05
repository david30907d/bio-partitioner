# type: ignore
"""
vcf partitioner
"""
import math
from abc import abstractclassmethod

import vcf

from bio_partitioner.base import PartitionerBase


class VCFPartitioner(PartitionerBase):
    @abstractclassmethod
    def count_num_of_rows(cls, dataset: str) -> int:
        num_of_rows = 0
        vcf_reader = vcf.Reader(open(dataset, "r"))
        for _ in vcf_reader:
            num_of_rows += 1
        return num_of_rows

    @abstractclassmethod
    def partition(cls, dataset: set, num_of_rows: int, partion_num: int):
        # type: ignore
        vcf_reader = vcf.Reader(open(dataset, "r"))
        rows_of_each_partition = math.ceil(num_of_rows / partion_num)

        partition_id = 0
        vcf_writer = vcf.Writer(open(f"{partition_id}.vcf", "w"), vcf_reader)
        for idx, row in enumerate(vcf_reader):
            vcf_writer.write_record(row)
            if idx and idx % rows_of_each_partition == 0:
                partition_id += 1
                vcf_writer = vcf.Writer(open(f"{partition_id}.vcf", "w"), vcf_reader)
