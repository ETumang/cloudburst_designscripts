
import json

datatypes = {"i":"image","t":"text"}

def write_data(): 

	meta = {}

	meta["uploader"] = "indi_scope"

	codebook = {"has_codebook":False}

	meta["dataset"] = raw_input("Dataset Title?\n")

	meta["type"] = datatypes[raw_input("Dataset Type?\nEnter t for text or i for image\n")]

	meta["tasks"] = (raw_input("What ML tasks would this dataset be good for?\nComma separated list please.\n")).split(',')

	meta["algorithms"] = (raw_input("Are there any algorithms associated with this dataset?\nComma separated list please.\n")).split(',')

	meta["description"] = raw_input("Enter a brief description for the dataset.\n")

	meta["collect"] = raw_input("When was the data collected?\n")

	meta["tags"] = raw_input("What content tags would you give the data?\n").split(',')

	meta["features"] = raw_input("What features does the data have?\n").split(',')

	meta["license"] = raw_input("Please input the license type.\n")

	codebook["has_codebook"] = True if raw_input("Does the dataset have a codebook?\nEnter y for yes and n for no.") == "y" else False

	if not codebook["has_codebook"]:
		for feat in meta["features"]:
			codebook[feat] = {"desc":"","rng":"","fmt":"","fmt_ins":""}
			codebook[feat]["desc"] = raw_input("Please enter a short description of feature "+feat+".\n")
			codebook[feat]["rng"] = raw_input("Please enter the feature's range, if applicable.\n")
			codebook[feat]["fmt"] = raw_input("Please enter the feature's format.\n")
			codebook[feat]["fmt_ins"] = raw_input("If the format is unusual, please enter instructions to read it.\n")
		codebook["notes"] = raw_input("Are there any useful things to know about this dataset?\n")
		codebook["methods"] = raw_input("How was the data collected?\n")
	else:
		codebook["location"] = raw_input("Where is the codebook located?\n")

	meta["codebook"] = codebook

	print("Done, thanks for the upload!")
	return meta

if __name__ == "__main__":
	filename = raw_input("Where do you want to save the metadata file?\n")

	with open(filename,'w+') as outfile:
		info = write_data()
		json.dump(info, outfile)



