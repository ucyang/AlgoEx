// Problem: http://codingdojang.com/scode/266?answer_mode=hide

#include <iostream>

using namespace std;

enum class Direction { LEFT, RIGHT, UP, DOWN };

int main()
{
	int** matrix;
	int r, c;
	int i, j;
	int count;
	int width;
	Direction dir;

	cin >> r >> c;
	if ((r < 2) || (c < 2))
		return 1;

	matrix = new int*[r];
	if (!matrix)
		return 2;

	for (i = 0; i < r; i++)
	{
		matrix[i] = new int[c];
		if (!matrix[i])
		{
			for (j = 0; j < i; j++)
				delete[] matrix[j];
			return 3;
		}
		memset(matrix[i], 0, c * sizeof(int));
	}

	i = j = 0;
	count = 1;
	dir = Direction::RIGHT;
	while (!matrix[i][j])
	{
		matrix[i][j] = count++;
		switch (dir)
		{
		case Direction::RIGHT:
			if ((j + 1 < c) && !matrix[i][j + 1])
				j++;
			else
			{
				dir = Direction::DOWN;
				i++;
			}
			break;
		case Direction::DOWN:
			if ((i + 1 < r) && !matrix[i + 1][j])
				i++;
			else
			{
				dir = Direction::LEFT;
				j--;
			}
			break;
		case Direction::LEFT:
			if ((j - 1 >= 0) && !matrix[i][j - 1])
				j--;
			else
			{
				dir = Direction::UP;
				i--;
			}
			break;
		case Direction::UP:
			if ((i - 1 >= 0) && !matrix[i - 1][j])
				i--;
			else
			{
				dir = Direction::RIGHT;
				j++;
			}
			break;
		}
	}

	count -= 2;
	width = 2;
	while (count /= 10)
		width++;

	for (i = 0; i < r; i++)
	{
		for (j = 0; j < c; j++)
		{
			cout.width(width);
			cout << matrix[i][j] - 1;
		}
		cout << endl;
	}

	for (i = 0; i < r; i++)
		delete[] matrix[i];
	delete[] matrix;
	return 0;
}
