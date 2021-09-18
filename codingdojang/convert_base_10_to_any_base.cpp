// Problem: http://codingdojang.com/scode/458?answer_mode=hide

#include <iostream>
#include <string>

using namespace std;

class Number
{
	friend ostream& operator<<(ostream& o, const Number& n)
	{
		return o << n.strNumber;
	}

	const char digits[17] = "0123456789ABCDEF";

	int number;
	int base;

	string strNumber;

	void Init(int aNumber, int aBase)
	{
		number = aNumber;
		base = aBase;

		strNumber.clear();
		do
		{
			strNumber += digits[aNumber % base];
		} while (aNumber /= base);

		reverse(strNumber.begin(), strNumber.end());
	}

public:
	Number(int aNumber = 0, int aBase = 10)
	{
		Init(aNumber, aBase);
	}

	int GetNumber() const
	{
		return number;
	}

	void SetNumber(int aNumber)
	{
		Init(aNumber, base);
	}

	int GetBase() const
	{
		return base;
	}

	void SetBase(int aBase)
	{
		Init(number, aBase);
	}

	void SetNumberAndBase(int aNumber, int aBase)
	{
		Init(aNumber, aBase);
	}
};

int main()
{
	Number number;
	int n, b;

	while (1)
	{
		cout << "Number: ";
		cin >> n;
		if (n < 0)
			break;
		
		cout << "Base: ";
		cin >> b;
		if ((b < 2) || (b > 16))
			break;

		number.SetNumberAndBase(n, b);
		cout << number << "\n\n";
	}
	return 0;
}