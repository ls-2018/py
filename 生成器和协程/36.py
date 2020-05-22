import decimal
import asyncio
import telnetlib

width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}")
print(1_000_000_000_000_000)
print(0x_FF_FF_FF_FF)
print('{:_}'.format(1000000))
print('{:_x}'.format(0xFFFFFFFF))


# 异步生成器
async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)


def condition():
    return True


# result = [i async
# for i in ticker(2, 3) if i % 2]
# result = [await fun()
# for fun in funcs if await condition()]


class IntField:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'expecting integer in {self.name}')
        instance.__dict__[self.name] = value

    # this is the new initializer:
    def __set_name__(self, owner, name):
        self.name = name


class Model:
    int_field = IntField()


tn = telnetlib.Telnet('www.baidu.com', 80)  # connect to finger port
tn.write(b'hello\r\n')
print(tn.read_all())
