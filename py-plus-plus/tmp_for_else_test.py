from pyplusplus.parser import parse_pyplusplus
from pyplusplus.compiler import execute_pyplusplus

source = '''sum = 0;
for (i in [1, 2, 3]) {
    sum = sum + i;
} else {
    sum = sum + 10;
}
print(sum);
'''
module = parse_pyplusplus(source)
execute_pyplusplus(module)
