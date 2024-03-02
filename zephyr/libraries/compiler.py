import os
import re

def compile():

    index_file = os.path.join(os.getcwd(), 'index.html')
    main_file = os.path.join(os.getcwd(), 'app/main.svelte')
    zephyr_file = os.path.join(os.getcwd(), 'zephyr/.index.html')

    with open(index_file, 'r') as file:
        index_content = file.read()

    with open(main_file, 'r') as file:
        main_content = file.read()

    components = re.findall(r'import (.*) from "(.*).svelte";', main_content)
    for component in components:
        component_name = component[0]
        component_file = os.path.join(os.getcwd(), f'{component[1].replace('./', 'app/')}.svelte')
        with open(component_file, 'r') as file:
            component_content = file.read()
        main_content = main_content.replace(f'<{component_name} />', component_content)
        main_content = re.sub(rf'import {component_name} from "(.*).svelte";', '', main_content)

    index_content = index_content.replace('@zephyr.content', main_content)

    with open(zephyr_file, 'w') as file:
        file.write(index_content)
