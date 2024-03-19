import sys
import gzip
import json
import pickle
import sniffles


class SNF2JSON(object):
    def dictify(self, obj) -> dict:
        """
        Check if the variable within the object is another object. If not it will return the object as a dictionary
        with the key as the variable name and the value as the variable value.
        :param obj: object to convert to dictionary
        :return: dictionary
        """
        tmp_dict = dict(obj.__dict__)
        tmp_dict = {k: v for k, v in tmp_dict.items() if v}
        for key, value in tmp_dict.items():
            if isinstance(value, set):
                tmp_dict[key] = list(value)
            # Determine if it is an object or regular data type
            if hasattr(value, "__dict__"):
                tmp_dict[key] = self.dictify(value)
        return tmp_dict

    def variant_candidates_to_dictionary(self, candidates: dict) -> dict:
        """
        Convert the variant candidates to a dictionary
        :param candidates: dictionary of variant candidates
        :return: dictionary
        """
        tmp_variant_dict = dict([(key, []) for key in candidates.keys()])
        for key, candidates in candidates.items():
            tmp_variants = []
            tmp_variant_dict[key] = tmp_variants
            for candidate in candidates:
                tmp_dict = self.dictify(candidate)
                tmp_variants.append(tmp_dict)
        return tmp_variant_dict

    def write_breakpoints_to_file(self, breakpoints: dict, output_file: str) -> None:
        """
        Write the breakpoints as a json file. Depending on the output file it will write to a gzip file
        or a normal file.
        :param breakpoints: dictionary of breakpoints
        :param output_file: output file
        :return: None
        """
        # if the outputfile contains gz then write to a gzip file otherwise write a normal file
        print(f"Writing breakpoints to {output_file}")
        if output_file.endswith(".gz"):
            with gzip.open(output_file, "wt") as file_handle:
                file_handle.write(json.dumps(breakpoints, indent="\t"))
        else:
            with open(output_file, "wt") as file_handle:
                file_handle.write(json.dumps(breakpoints, indent="\t"))

    def main(self, snf_file, output_file) -> None:
        """
        Main function to convert the snf file to a json file.
        :param snf_file: Path to Sniffles snf file
        :param output_file: Output path for the SNFJ like file
        :return:
        """
        file_handle = open(snf_file, "rb")
        header_text = file_handle.readline()
        header_length = len(header_text)
        header = json.loads(header_text)
        # get breakpoint index
        _index = header["index"]
        blocks = {}

        # breakpoint data 
        breakpoint_data = {}
        selected_variant_keys = ['DEL', 'INS', 'INV', 'DUP', 'BND']

        # read blocks for each contig
        for contig in _index.keys():
            print(f"Converting contig {contig}")
            for block_start in _index[contig].keys():

                # read blocks
                block_index = block_start
                for block_data_start, block_data_length in _index[contig][block_index]:
                    try:
                        file_handle.seek(header_length + block_data_start)
                        data = gzip.decompress(file_handle.read(block_data_length))
                        # deserialize the data
                        block_data = pickle.loads(data)
                        if contig not in blocks.keys():
                            blocks[contig] = []
                        blocks[contig].append(block_data)

                        # testing block data
                        # only select from the blocks dictionary the keys DEL, INS, INV, DUP, BND
                        trimmed_block_data = {k: block_data[k] for k in selected_variant_keys if k in block_data}
                        # coverage data is discarded
                        variant_dict = self.variant_candidates_to_dictionary(trimmed_block_data)

                        # check if the key exists in the breakpoint_data dictionary
                        if contig not in breakpoint_data.keys():
                            breakpoint_data[contig] = {}
                            # check if the selected_variant_keys exists in the breakpoint_data[contig] dictionary if
                            # not add them as empty lists
                            for variant in selected_variant_keys:
                                if variant not in breakpoint_data[contig].keys():
                                    breakpoint_data[contig][variant] = []
                        # append the block data to the breakpoint_data
                        for variant, data in variant_dict.items():
                            breakpoint_data[contig][variant] += data

                    except Exception as e:
                        print(f"Error reading contig {contig} block {block_index} data: {e}")
                        raise e
        file_handle.close()
        # write the breakpoint data to snfspc file
        self.write_breakpoints_to_file(breakpoints=breakpoint_data, output_file=output_file)


def main():
    # Write help message
    help = """
        SNF2JSON: Convert Sniffles SNFJ file to a JSON file.
        
        Usage to convert a snf file to a snfj (JSON) file:
        Regular:    snf_to_spectre.py <input_file.snf> <output_file.snfj>
        Compressed: snf_to_spectre.py <input_file.snf> <output_file.snfj.gz>
        """
    # write --help message
    if "-h" in sys.argv or "--help" in sys.argv:
        print(help)
        sys.exit(0)
    # Check if two arguments are provided
    if len(sys.argv) != 3:
        print(help)
        sys.exit(1)

    # Run pipeline
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    sj = SNF2JSON()
    sj.main(input_file, output_file)


if __name__ == "__main__":
    main()
