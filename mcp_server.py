"""MCP Server for Normalized Compression Distance Skill."""
import json
import sys
from client import NCDCalculator

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "calculate_ncd",
                            "description": "Calculate Normalized Compression Distance between texts or a matrix",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "text1": {"type": "string"},
                                    "text2": {"type": "string"},
                                    "items": {"type": "array", "items": {"type": "string"}},
                                    "labels": {"type": "array", "items": {"type": "string"}}
                                }
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                if "text1" in args and "text2" in args:
                    out = {"distance": NCDCalculator.distance(args["text1"], args["text2"])}
                elif "items" in args:
                    out = NCDCalculator.distance_matrix(args["items"], args.get("labels"))
                else:
                    out = {"error": "Invalid arguments"}

                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(out)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
