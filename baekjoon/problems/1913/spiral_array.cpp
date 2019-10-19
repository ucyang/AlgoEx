// Problem: https://www.acmicpc.net/problem/1913

#include <iostream>
#include <cstring>

using namespace std;

enum class Direction { LEFT, RIGHT, UP, DOWN };

int main()
{
	int** matrix;
	int r, c;
	int i, j;
	int n;
	int n_x, n_y;
	int count;
	Direction dir;

	cin >> r;
	c = r;
	if ((r < 0) || (c < 0))
		return 0x1;
	cin >> n;

	matrix = new int*[r];
	if (!matrix)
		return 0x2;

	for (i = 0; i < r; i++)
	{
		matrix[i] = new int[c];
		if (!matrix[i])
		{
			for (j = 0; j < i; j++)
				delete[] matrix[j];
			return 0x3;
		}
		memset(matrix[i], 0, c * sizeof(int));
	}

	i = j = 0;
	count = r * c;
	dir = Direction::DOWN;
	while (!matrix[i][j])
	{
		matrix[i][j] = count--;
		switch (dir)
		{
		case Direction::RIGHT:
			if ((j + 1 < c) && !matrix[i][j + 1])
				j++;
			else
			{
				dir = Direction::UP;
				i--;
			}
			break;
		case Direction::DOWN:
			if ((i + 1 < r) && !matrix[i + 1][j])
				i++;
			else
			{
				dir = Direction::RIGHT;
				j++;
			}
			break;
		case Direction::LEFT:
			if ((j - 1 >= 0) && !matrix[i][j - 1])
				j--;
			else
			{
				dir = Direction::DOWN;
				i++;
			}
			break;
		case Direction::UP:
			if ((i - 1 >= 0) && !matrix[i - 1][j])
				i--;
			else
			{
				dir = Direction::LEFT;
				j--;
			}
			break;
		}
	}

	n_x = n_y = -1;
	for (i = 0; i < r; i++)
	{
		for (j = 0; j < c; j++)
		{
			if (matrix[i][j] == n)
				n_x = j + 1, n_y = i + 1;
			if (j)
				cout << " ";
			cout << matrix[i][j];
		}
		cout << endl;
	}
	cout << n_y << " " << n_x << endl;

	for (i = 0; i < r; i++)
		delete[] matrix[i];
	delete[] matrix;

	return 0;
}
