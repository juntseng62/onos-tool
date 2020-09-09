import sys
import json

def main():
    in_file = sys.argv[1]
    component = sys.argv[2]
    with open(in_file, 'r') as f:
        data = json.load(f)
    
    
    print(json.dumps(data[component], 4))

    with open(in_file, 'w') as f:
        json.dump(data[component], f)

if __name__ == "__main__":
    main()
