# Note that this has experimental features added, they are flagged
jobspec_v2 = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "http://github.com/flux-framework/rfc/tree/master/data/spec_24/schema.json",
    "title": "jobspec-01",
    "description": "Flux jobspec version 1",
    "definitions": {
        "intranode_resource_vertex": {
            "description": "schema for resource vertices within a node, cannot have child vertices",
            "type": "object",
            "required": ["type", "count"],
            "properties": {
                "type": {"enum": ["core", "gpu"]},
                "count": {"type": "integer", "minimum": 1},
                "unit": {"type": "string"},
            },
            "additionalProperties": False,
        },
        "node_vertex": {
            "description": "schema for the node resource vertex",
            "type": "object",
            "required": ["type", "count", "with"],
            "properties": {
                "type": {"enum": ["node"]},
                "count": {"type": "integer", "minimum": 1},
                "unit": {"type": "string"},
                "with": {
                    "type": "array",
                    "minItems": 1,
                    "maxItems": 1,
                    "items": {
                        "oneOf": [
                            {"$ref": "#/definitions/slot_vertex"},
                            {"$ref": "#/definitions/intranode_resource_vertex"},
                        ]
                    },
                },
            },
            "additionalProperties": False,
        },
        "slot_vertex": {
            "description": "special slot resource type - label assigns to task slot",
            "type": "object",
            "required": ["type", "count", "with", "label"],
            "properties": {
                "type": {"enum": ["slot"]},
                "count": {"type": "integer", "minimum": 1},
                "unit": {"type": "string"},
                "label": {"type": "string"},
                "exclusive": {"type": "boolean"},
                "with": {
                    "type": "array",
                    "minItems": 1,
                    "maxItems": 2,
                    "items": {"oneOf": [{"$ref": "#/definitions/intranode_resource_vertex"}]},
                },
            },
            "additionalProperties": False,
        },
    },
    "type": "object",
    "required": ["version", "resources", "task"],
    "properties": {
        "version": {
            "description": "the jobspec version",
            "type": "integer",
            "enum": [1],
        },
        "resources": {
            "description": "requested resources",
            "type": "array",
            "minItems": 1,
            "maxItems": 1,
            "items": {
                "oneOf": [
                    {"$ref": "#/definitions/node_vertex"},
                    {"$ref": "#/definitions/slot_vertex"},
                ]
            },
        },
        "attributes": {
            "description": "system and user attributes",
            "type": ["object", "null"],
            "properties": {
                "system": {
                    "type": "object",
                    "properties": {
                        "duration": {"type": "number", "minimum": 0},
                        "cwd": {"type": "string"},
                        "environment": {"type": "object"},
                    },
                },
                "user": {"type": "object"},
            },
            "additionalProperties": False,
        },
        "task": {
            "description": "task configuration",
            "type": "object",
            # I changed this so if no slot is defined, it's
            # implied to be at the top level (the node) which isn't allowed
            # by this super strict jobspec
            "required": ["count"],
            "properties": {
                "command": {
                    "type": ["string", "array"],
                    "minItems": 1,
                    "items": {"type": "string"},
                },
                # This could be embedded as a yaml file, and then
                # executed with jobspec <yaml> if it's not wanted here
                "transform": {
                    "type": ["array"],
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "properties": {
                            "step": {"type": "string"},
                        },
                        "required": ["step"],
                    },
                },
                # RESOURCES AND SCRIPTS ARE EXPERIMENTAL
                "resources": {"type": "object"},
                "scripts": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["name", "content"],
                        "properties": {
                            "name": {"type": "string"},
                            "content": {"type": "string"},
                        },
                    },
                },
                "slot": {"type": "string"},
                "count": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "per_slot": {"type": "integer", "minimum": 1},
                        "total": {"type": "integer", "minimum": 1},
                    },
                },
            },
            "additionalProperties": False,
        },
    },
}

jobspec_v1 = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "http://github.com/flux-framework/rfc/tree/master/data/spec_24/schema.json",
    "title": "jobspec-01",
    "description": "Flux jobspec version 1",
    "definitions": {
        "intranode_resource_vertex": {
            "description": "schema for resource vertices within a node, cannot have child vertices",
            "type": "object",
            "required": ["type", "count"],
            "properties": {
                "type": {"enum": ["core", "gpu"]},
                "count": {"type": "integer", "minimum": 1},
                "unit": {"type": "string"},
            },
            "additionalProperties": False,
        },
        "node_vertex": {
            "description": "schema for the node resource vertex",
            "type": "object",
            "required": ["type", "count", "with"],
            "properties": {
                "type": {"enum": ["node"]},
                "count": {"type": "integer", "minimum": 1},
                "unit": {"type": "string"},
                "with": {
                    "type": "array",
                    "minItems": 1,
                    "maxItems": 1,
                    "items": {"oneOf": [{"$ref": "#/definitions/slot_vertex"}]},
                },
            },
            "additionalProperties": False,
        },
        "slot_vertex": {
            "description": "special slot resource type - label assigns to task slot",
            "type": "object",
            "required": ["type", "count", "with", "label"],
            "properties": {
                "type": {"enum": ["slot"]},
                "count": {"type": "integer", "minimum": 1},
                "unit": {"type": "string"},
                "label": {"type": "string"},
                "exclusive": {"type": "boolean"},
                "with": {
                    "type": "array",
                    "minItems": 1,
                    "maxItems": 2,
                    "items": {"oneOf": [{"$ref": "#/definitions/intranode_resource_vertex"}]},
                },
            },
            "additionalProperties": False,
        },
    },
    "type": "object",
    "required": ["version", "resources", "attributes", "tasks"],
    "properties": {
        "version": {
            "description": "the jobspec version",
            "type": "integer",
            "enum": [1],
        },
        "resources": {
            "description": "requested resources",
            "type": "array",
            "minItems": 1,
            "maxItems": 1,
            "items": {
                "oneOf": [
                    {"$ref": "#/definitions/node_vertex"},
                    {"$ref": "#/definitions/slot_vertex"},
                ]
            },
        },
        "attributes": {
            "description": "system and user attributes",
            "type": ["object", "null"],
            "properties": {
                "system": {
                    "type": "object",
                    "properties": {
                        "duration": {"type": "number", "minimum": 0},
                        "cwd": {"type": "string"},
                        "environment": {"type": "object"},
                    },
                },
                "user": {"type": "object"},
            },
            "additionalProperties": False,
        },
        "tasks": {
            "description": "task configuration",
            "type": "array",
            "maxItems": 1,
            "items": {
                "type": "object",
                "required": ["slot", "count", "command"],
                "properties": {
                    "command": {
                        "type": ["string", "array"],
                        "minItems": 1,
                        "items": {"type": "string"},
                    },
                    "slot": {"type": "string"},
                    "count": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "per_slot": {"type": "integer", "minimum": 1},
                            "total": {"type": "integer", "minimum": 1},
                        },
                    },
                },
                "additionalProperties": False,
            },
        },
    },
}
