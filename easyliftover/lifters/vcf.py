from .abstract import AbstractRowWiseTextLifter


class VcfLifter(AbstractRowWiseTextLifter):
    """Lifter for bed files."""

    def __lift_row__(self, row: str) -> "str | None":
        """Lifts a single row."""

        chromosome, pos, *rest = row.split()

        lifted = self.convert_coordinate(chromosome, int(pos))

        if lifted is not None:
            lifted_chromosome, lifted_pos = lifted

            return "\t".join(
                [
                    lifted_chromosome,
                    str(lifted_pos),
                    *rest,
                ]
            )
        else:
            return None

    @staticmethod
    def supported_formats() -> list:
        """Returns the supported formats."""
        return ["vcf"]
