import csv

input_file = "dataset/raw/1429_1.csv"
output_file = "dataset/processed_reviews.tsv"

count = 0

def clean(value):
    return value.strip().replace("\t", " ").replace("\n", " ").replace("\r", " ")

with open(input_file, "r", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)

    with open(output_file, "w", encoding="utf-8") as outfile:

        for row in reader:
            product_id = clean(row["id"])
            product_name = clean(row["name"])
            category = clean(row["categories"])
            rating = clean(row["reviews.rating"])

            if product_id and category and rating:
                outfile.write(
                    f"{product_id}\t{product_name}\t{category}\t{rating}\n"
                )
                count += 1

print("Preprocessing completed!")
print("Total records:", count)
