from string import Template

class View():
    def __init__(self) -> None:
        pass

    def generate_jsx_view_str(name: str) -> str:
        class_name = name.lower()
        jsx = '''
import * as React from "react";
import './$name';
export default function $name () {
    return (
         <div className="$class_name-container">$name</div>
    )
}
'''
        return Template(jsx).substitute(name=name, class_name=class_name)

    def generate_index_file(name: str) -> str:
        index = """export {default} from './$name';"""
        return Template(index).substitute(name=name)