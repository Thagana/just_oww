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
    
    def generate_test_file(name: str) -> str:
        content = """import React from 'react';
import ReactDOM from 'react-dom';
import $name from './$name';

it('It should mount', () => {
  const div = document.createElement('div');
  ReactDOM.render(<$name />, div);
  ReactDOM.unmountComponentAtNode(div);
});
        """
        return Template(content).substitute(name=name)