from Moduls.moduls_filter_fastq import (
    check_quality,
    check_gc,
    check_lenght,
    read_fastq
)
from Moduls.moduls_dna_rna_tools import (
    transcribe,
    reverse,
    complement,
    reverse_complement,
    verification,
)


def filter_fastq(
    input_fastq, output_fastq, gc_bounds=(0, 100), length_bounds=(0, 2 ** 32), quality_threshold=0
):
    seqs = read_fastq(input_fastq)
    new_sq = check_quality(seqs, quality_threshold)
    seqs_after_gc = check_gc(new_sq, gc_bounds)
    seqs_after_lenght = check_lenght(seqs_after_gc, length_bounds)
    write_fastq(output_fastq, seqs_after_lenght)


def run_dna_rna_tools(*args):

    *na, func_name = args

    verification(na)

    if func_name == "transcribe":
        func = transcribe
    elif func_name == "reverse":
        func = reverse
    elif func_name == "complement":
        func = complement
    elif func_name == "reverse_complement":
        func = reverse_complement
    else:
        print("Error")

    result = func(na)
    if len(result) == 1:
        return " ".join(result)
    else:
        return result
