# DNA -> RNA Transcription

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()

def transcribe(seq: str, reverse: bool = False) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    if isinstance(seq, str) is False:
        raise ValueError("Seq must be of type string.")

    if seq == "":
        raise ValueError("Seq can't be an empty string.")

    seq = seq.upper()

    if reverse:
        seq = seq[::-1]

    for idx, nuc in enumerate(seq):
        if nuc not in ALLOWED_NUC:
            err = f"Nucleotide {nuc} at position {idx+1} for {seq} was not an allowed DNA nucleotide."
            if reverse:
                err = err[:-1]  # remove period
                err += "(reversed sequence)."

            raise ValueError(
                f"Nucleotide {nuc} at position {idx+1} for {seq} was not an allowed DNA nucleotide."
            )
    return "".join(map(TRANSCRIPTION_MAPPING.get, seq))




def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA then reverses
    the strand
    """
    return transcribe(seq, reverse=True)
