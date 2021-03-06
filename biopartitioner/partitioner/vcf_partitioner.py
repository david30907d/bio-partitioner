"""
vcf partitioner
"""
import math

import vcf

from biopartitioner.base import PartitionerBase


class VCFPartitioner(PartitionerBase):
    def _count_num_of_rows(self) -> int:
        num_of_rows = 0
        vcf_reader = vcf.Reader(open(self.dataset, "r"))
        for _ in vcf_reader:
            num_of_rows += 1
        return num_of_rows

    def partition(self):
        vcf_reader = vcf.Reader(open(self.dataset, "r"))
        rows_of_each_partition = math.ceil(self.num_of_rows / self.partition_num)

        partition_id = 0
        vcf_writer = self._get_vcf_writer(partition_id, vcf_reader)
        for idx, row in enumerate(vcf_reader):
            vcf_writer.write_record(row)
            if idx and idx % rows_of_each_partition == 0:
                partition_id += 1
                vcf_writer = self._get_vcf_writer(partition_id, vcf_reader)

    def _get_vcf_writer(self, partition_id, vcf_reader):
        partition_filepath = self.working_dir.joinpath(f"{partition_id}.vcf")
        return vcf.Writer(open(f"{partition_filepath}", "w"), vcf_reader,)
