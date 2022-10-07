from string import Template

class Component ():
    def __init__(self) -> None:
        pass

    def component_generator(name: str) -> str:
        jsx = '''import * as React from "react";
import './$name';
export default function $name () {
    return (
         <div>$name</div>
        )
}
'''
        return Template(jsx).substitute(name=name)

    def generate_index(name: str) -> str:
        index = """export {default} from './$name';"""
        return Template(index).substitute(name=name)
