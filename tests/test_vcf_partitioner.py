from pathlib import Path

from bio_partitioner.factory import PartitionerFactory


def test_crawl_every_page():
    partitioner = PartitionerFactory.create_partitioner("vcf")
    dataset = "fixtures/scaffold.vcf"
    num_of_rows = partitioner.count_num_of_rows(dataset)
    partitioner.partition(dataset, num_of_rows, 10)
    if __debug__:
        for idx in range(10):
            if not Path(f"{idx}.vcf").exists():
                raise AssertionError(f"{idx}.vcf not found!")
