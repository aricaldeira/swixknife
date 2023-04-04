# SwixKnife
SwixKnife - Python classes and function to deal with Sezimal (base 6) numbers - also known as Seximal
### What’s Sezimal/Seximal?
* [Senary](https://en.wikipedia.org/wiki/Senary)
* [seximal.net](https://www.seximal.net/)
* [a better way to count](https://www.youtube.com/watch?v=qID2B4MK7Y0)
* [seximal responses](https://www.youtube.com/watch?v=wXeX_XKSNlc)
* [xanthir.com/hex](https://xanthir.com/hex)
* [Shack's Base Six Dialectic](http://shacktoms.org/base-six/base-six.htm)
* [Learn to count in Seximal, a position above the rest](https://hackaday.com/2018/07/20/learn-to-count-in-seximal-its-a-position-above-the-rest/)
* [Math is fun - Senary](https://www.mathsisfun.com/definitions/senary.html)

### What’s in here and how to use it
There are 3 classes in this lib:
* Sezimal - similar to the Decimal class
* SezimalInteger - It works the same as Sezimal, but only allows integers
* SezimalFraction - similar to the Fraction class

They are interoperable with int, float and Decimal, within the following principles:
* Decimal objects are converted to Sezimal objects
* int and float are treated as if they were Sezimal, so, using the decimal digits 6789 will give you an error
* to convert a base 14 (10₁₄) int or float, convert them to a Decimal before

Default precision is 100 (36₁₄) sezimal places, that is equivalent to Decimal’s default 44 (28₁₄) decimal places.

Operators + - * / % are all evaluated without converting back and forth to Decimal.

Operator ** uses Decimal only for fractional exponents (roots).

*Functions exp, ln, log, log2, log14, sqrt, all use Decimal to execute the actual calculations, and convert back to Sezimal for the answer, because they all use calculus methods to aproximate the answers, and those are yet to be converted to use pure Sezimal operations.*

The basic operators work as expected:

    >>> from swixknife import *
    >>> x = Sezimal(14)  # 14 is Decimal('10')
    >>> y = Sezimal(0.3)  # 0.3 is Decimal('0.5')
    >>> z = Sezimal(0.6789)  # This gives an error, 6789 are not Sezimal digits
    ValueError: The number 0.6789 has an invalid format for a sezimal number
    >>> from decimal import Decimal
    >>> z = Sezimal(Decimal('0.6789'))  # This works, we explicity know that 0.6789 is a Decimal
    >>> f = SezimalFraction(3.2)  # or
    >>> f = SezimalFraction(14, 3)  # or
    >>> f = SezimalFraction('14/3')
    >>> x + y
    Sezimal('14.3')
    >>> x - y
    Sezimal('13.3')
    >>> x * y
    Sezimal('5')
    >>> x / y
    Sezimal('32')
    >>> x / (y * 10)  # 10 is treated as Decimal('6')
    Sezimal('3.2')
    >>> x ** 2
    Sezimal('244')
    >>> x % 4
    Sezimal('2')
    >>> f * 10
    Sezimal('32.0')
    >>> f / 14
    Sezimal('0.2')
    >>> SezimalFraction(f / 14)
    SezimalFraction('1/3')
    >>> f / 14
    Sezimal('0.2')
    >>> x += 43
    >>> x
    Sezimal('101')

Also, Sezimal objects have the following methods/properties:

    >>> from swixknife import *
    >>> x = Sezimal(123450.012345)
    >>> x.decimal
    Decimal('11190.399734....  # a lot of decimal places
    >>> x.formatted_number
    '12_3450.0123_45'
    >>> Sezimal(3.2).as_integer_ratio()
    (Sezimal('14'), Sezimal('3'))
    >>> Sezimal(14).factorial()
    Sezimal('2_0544_0000')
    >>> Sezimal(100).ln()  # Natural logarithm
    Sezimal('3.3300_1235_4245_5414_4234_5013_3035_4200_0312')
    >>> Sezimal(100).log()  # Sezimal (base six) logarithm
    Sezimal('2')
    >>> Sezimal(100).log2()  # Base 2 logarithm
    Sezimal('5.1004_1200_4301_3301_2143_4143_2523_2423_5041')
    >>> Sezimal(100).log14()  # Decimal (base ten) logarithm
    Sezimal('1.3200_5450_3253_0505_0505_3032_5511_2323_0533')
    >>> Sezimal(10_000).sqrt()  # Square root
    Sezimal('100.0')
    >>> Sezimal(1.4430_0415).exp()  # Euler’s number elevated to the power
    Sezimal('5.5555_5550_4330_0510_0220_2125_2222_0022_0112')
