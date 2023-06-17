from .abstract import AbstractLifter


class WigLifter(AbstractLifter):
    def lift(self, data: str) -> str:
        result = []

        chromosome: str | None = None

        for line in data.splitlines():
            splitted = line.split()

            if splitted[0] in ("fixedStep", "variableStep"):
                key_value = {
                    key: value
                    for key, value in [entry.split("=") for entry in splitted[1:]]
                }
                if splitted[0] == "variableStep":
                    chromosome = key_value["chrom"]
                    result.append(line)
                else:
                    chromosome = key_value["chrom"]
                    start = int(key_value["start"])

                    lifted = self.convert_coordinate(chromosome, start)

                    if lifted is None:
                        continue

                    lifted_chromosome = lifted[0]
                    lifted_start = lifted[1]

                    key_value["chrom"] = lifted_chromosome
                    key_value["start"] = str(lifted_start)

                    result.append(
                        "fixedStep "
                        + " ".join(
                            [f"{key}={value}" for key, value in key_value.items()]
                        )
                    )

                    chromosome = None

            elif chromosome is not None:
                start = int(splitted[0])

                lifted = self.convert_coordinate(chromosome, start)

                if lifted is None:
                    continue

                lifted_start = lifted[1]

                splitted[0] = str(lifted_start)

                result.append(" ".join(splitted))

            else:
                result.append(line)

        return "\n".join(result)
