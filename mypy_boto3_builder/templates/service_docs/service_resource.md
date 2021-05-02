# {{ package.service_resource.name }} for boto3 {{ package.service_name.class_name }} module

> [Index](../index.md) > [{{ package.service_name.class_name }}](./index.md) > {{ package.service_resource.name }}

Auto-generated documentation for [{{ package.service_name.class_name }}]({{ package.service_name.doc_link}})
type annotations stubs module [{{ package.service_name.module_name }}]({{ package.service_name.pypi_link }}).

## {{ package.service_resource.name }}

Type annotations for `boto3.resource("{{ package.service_name.boto3_name }}")`, included resources and collections.

Can be used directly:

```python
from {{ package.service_name.module_name }}.service_resource import {{ package.service_resource.name }}
```


{% if package.service_resource.methods %}
## Methods
{% for method in package.service_resource.methods %}
### {{ package.service_resource.name }}.{{ method.name }}

Type annotations for `boto3.resource("{{ package.service_name.boto3_name }}").{{ method.name }}` method.

{{ method.docstring }}

Definition:

```python
{% with render_docstrings=False -%}
{% include "common/method.py.jinja2" with context -%}{{ '\n' -}}
{% endwith -%}
```
{% endfor %}
{% endif %}

{% if package.service_resource.collections %}
## Collections
{% for collection in package.service_resource.collections %}
### {{ package.service_resource.name }}.{{ collection.attribute_name }}

Type annotations for `boto3.resource("{{ package.service_name.boto3_name }}").{{ collection.attribute_name }}` collection.

Can be used directly:

```python
from {{ package.service_name.module_name }}.service_resource import {{ collection.name }},

def get_collection() -> {{ collection.name }}:
    return boto3.resource("{{ package.service_name.boto3_name }}").{{ collection.attribute_name }}(
        ...
    )
```

{{ collection.docstring }}

Definition:

```python
{% with class=collection, render_docstrings=False -%}
{% include "common/class.py.jinja2" with context -%}{{ '\n' -}}
{% endwith -%}
```
{% endfor %}
{% endif %}

{% for resource in package.service_resource.sub_resources %}
## {{ resource.name }}

Type annotations for `boto3.resource("{{ package.service_name.boto3_name }}").{{ resource.name }}` class.

Can be used directly:

```python
from {{ package.service_name.module_name }}.service_resource import {{ resource.name }}

def get_resource() -> {{ resource.name }}:
    return boto3.resource("{{ package.service_name.boto3_name }}").{{ resource.name }}(...)
```

{{ resource.docstring }}

{% if resource.attributes %}
### {{ resource.name }} attributes

{% for attribute in resource.attributes %}
- `{{ attribute.name }}`: `{{ attribute.type_annotation.render() }}`
{% else %}
{{ resource.name }} has no attributes.
{% endfor %}
{% endif %}

{% if resource.methods %}
### {{ resource.name }} methods

{% for method in resource.methods %}
#### {{ resource.name }}.{{ method.name }}

Type annotations for `boto3.resource("{{ package.service_name.boto3_name }}").{{ method.name }}` method.

{{ method.docstring }}

```python
{% with render_docstrings=False -%}
{% include "common/method.py.jinja2" with context -%}{{ '\n' -}}
{% endwith -%}
```
{% endfor %}
{% endif %}

{% if resource.collections %}
### {{ resource.name }} collections

{% for collection in resource.collections %}
#### {{ resource.name }}.{{ collection.attribute_name }}

Type annotations for `boto3.resource("{{ package.service_name.boto3_name }}").{{ resource.name }}(...).{{ collection.attribute_name }}` collection.

Can be used directly:

```python
from {{ package.service_name.module_name }}.service_resource import {{ collection.name }},

def get_collection() -> {{ collection.name }}:
    resource = boto3.resource("{{ package.service_name.boto3_name }}").{{ resource.name }}(...)
    return resource.{{ collection.attribute_name }}
```

{{ collection.docstring }}

```python
{% with class=collection, render_docstrings=False -%}
{% include "common/class.py.jinja2" with context -%}{{ '\n' -}}
{% endwith -%}
```
{% endfor %}
{% endif %}

{% endfor %}