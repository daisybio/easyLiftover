from .abstract import AbstractRowWiseLifter


class BedLifter(AbstractRowWiseLifter):
    """Lifter for bed files."""

    def __lift_row__(self, row: str) -> "str | None":
        """Lifts a single row."""

        chromosome, start, end, *rest = row.split()

        lifted = self.convert_region(chromosome, int(start), int(end))

        if lifted is not None:
            lifted_chromosome, lifted_start, lifted_end = lifted

            return "\t".join(
                [
                    lifted_chromosome,
                    lifted_start,
                    lifted_end,
                    *rest,
                ]
            )
        else:
            return None
