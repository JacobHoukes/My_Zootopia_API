import data_fetcher


def serialize_animal(animal_obj):
    """This function serializes a single animal object into HTML."""
    name_diet_location_type = ''
    name_diet_location_type += '<li class="cards__item">\n'  # List item tag instead of <article>
    name_diet_location_type += f'<header><h2 class="card__title">{animal_obj["name"]}</h2></header>\n'
    name_diet_location_type += f'<section class="card__content">\n'
    name_diet_location_type += f'<p><strong>Diet: </strong>{animal_obj["characteristics"]["diet"]}</p>\n'
    name_diet_location_type += f'<p><strong>Location: </strong>{animal_obj["locations"][0]}</p>\n'
    if "type" in animal_obj["characteristics"]:
        name_diet_location_type += f'<p><strong>Type: </strong>{animal_obj["characteristics"]["type"]}</p>\n'
    name_diet_location_type += '</section>\n'
    name_diet_location_type += '</li>\n'  # Close the <li> tag instead of <article>
    return name_diet_location_type


def get_animal_info(animals_list):
    """This function returns the animal's name, diet, location, and if available, type in HTML format."""
    name_diet_loc_type = "<ul>"  # Start with an unordered list
    for animal in animals_list:
        name_diet_loc_type += serialize_animal(animal)
    name_diet_loc_type += "</ul>"  # Close the unordered list
    return name_diet_loc_type


def read_html(file_path, formatted_data):
    """This function reads the HTML template file and replaces the placeholder with formatted data."""
    with open(file_path, "r", encoding='utf-8') as file:
        html_template = file.read()
        actual_animal_data = html_template.replace("__REPLACE_ANIMALS_INFO__", formatted_data)
        return actual_animal_data


def write_html(file_path, new_content):
    """This function writes new content into the HTML file."""
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(new_content)


def main():
    """This function fetches animal data from the API, inserts it into the HTML template, and writes the result to a new HTML file."""
    animal_name = input("Please enter an animal: ").strip()
    data = data_fetcher.fetch_data(animal_name)

    if data:
        formatted_data = get_animal_info(data)
    else:
        formatted_data = f'<h2 style="color:red;">The animal "{animal_name}" doesn\'t exist.</h2>'

    filled_template = read_html("animals_template.html", formatted_data)
    write_html("animals.html", filled_template)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
