from .abstract import AbstractRowWiseTextLifter


class GffLifter(AbstractRowWiseTextLifter):
    """Lifter for gff files."""

    def __lift_row__(self, row: str) -> "str | None":
        splitted = row.split()

        chromosome = splitted[0]
        start = splitted[3]
        end = splitted[4]

        lifted = self.convert_region(chromosome, int(start), int(end))

        if lifted is not None:
            lifted_chromosome, lifted_start, lifted_end = lifted

            splitted[0] = lifted_chromosome
            splitted[3] = str(lifted_start)
            splitted[4] = str(lifted_end)

            return "\t".join(splitted)

        else:
            return None
