import click
import math
import sys
import struct


@click.command()
@click.help_option('-h', '--help')
@click.option('-b', '--bytes', default=20000, type=int, help='Number of bytes to generate. Max 2,147,483,647 on 32 bit '
                                                             'machines')
@click.option('-w', '--width', default=32, type=click.Choice([32, 64]), help='32 bit or 64 bit')
@click.option('-o', '--offset', help='Search for a given set of bytes')
@click.option('-v', '--verbose', count=True, help='Show debug message etc')
@click.version_option('1.0', '--version', message='%(prog)s v%(version)s')
def main(bytes, width, offset, verbose):
    """
    Main Logic
    :param bytes: integer
    :param offset: string
    """
    global verbosity
    verbosity = verbose

    if bytes is not None:
        gen_bytes(bytes, width)


def msg(message):
    if verbosity >= 1:
        click.echo(message)


def gen_bytes(bytes_requested, sys_bit_width):
    """
    Generate random unique number of bytes requested
    :param bytes_requested: integer
    :param sys_bit_width: 32 or 64
    """
    msg("Generating {} Requested Bytes".format(bytes_requested))

    generated_bytes = bytearray()
    byte_count = 0

    bytes_per_num = int(sys_bit_width / 8)
    msg("Bytes Per Number {}".format(bytes_per_num))
    nums_required = bytes_requested / bytes_per_num
    msg("Numbers Required {}".format(nums_required))

    if (nums_required % bytes_per_num) != 0:
        nums_required = int(math.ceil(nums_required))
        msg("Numbers Required Rounded Up To {}".format(nums_required))

    # Create loop that counts from 0 to our number
    for i in range(0, int(nums_required)):
        if sys_bit_width == 32:
            msg("Generated 32 Bits: {:032b} \t Hex: {}".format(i, hex(i)))
        elif sys_bit_width == 64:
            msg("Generated 64 Bits: {:064b} \t Hex: {}".format(i, hex(i)))

        bin_num = struct.pack('=I', i)
        generated_bytes.extend(bin_num)
        byte_count += bytes_per_num

    msg("Completed. Outputting {} bytes".format(byte_count))

    sys.stdout.buffer.write(generated_bytes)


if __name__ == '__main__':
    main()
