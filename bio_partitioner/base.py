from abc import ABCMeta, abstractclassmethod


class PartitionerBase(metaclass=ABCMeta):
    @abstractclassmethod
    def partition(cls, dataset: set, num_of_rows: int, partion_num: int) -> None:
        pass

    @abstractclassmethod
    def count_num_of_rows(cls, dataset: str) -> int:
        pass
