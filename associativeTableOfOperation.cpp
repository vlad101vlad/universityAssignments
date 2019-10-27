// project3_algebra.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>

using namespace std;

ofstream fout("test0.out");

int set[10];
int operationSet[20];
int operationMatrix[20][20];
int n;
int counter;

void printSet(int set[], int n);
void get_all_operations(int n, int index);
void get_operation_matrix(int operationSet[], int n);

int main()
{
	cin >> n;
	fout << "These are the operation table for the given set: "<<endl;
	for (int i = 1; i <= n; i++)
		set[i] = i;
	
	///printSet(set, n);
	get_all_operations(n, 1);
	fout << "There are " << counter << " associative operations for the set A={ ";
	for (int i = 1; i <= n; i++)
	{
		fout << "a" << set[i] << " ";
		if (i != n)
			fout << ",";
	}
		
	fout << "}";

}

void printSet(int set[], int n)
{
	for (int i = 1; i <= n; i++)
		cout << set[i] << " ";
}

void get_all_operations(int n, int index)
{
	if (index > n* n)
	{
		get_operation_matrix(operationSet, n);

		int ok = 1;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				for (int k = 1; k <= n; k++)
					if (operationMatrix[operationMatrix[i][j]][k] != operationMatrix[i][operationMatrix[j][k]])
						ok = 0;
		if (ok == 1)
		{
			for (int i = 1; i <= n; i++)
			{
				for (int j = 1; j <= n; j++)
					fout << "a" << operationMatrix[i][j] << " ";
				fout << endl;
			}
			fout << endl;
			counter++;
		}
		
	}		
	else
		for (int i = 1; i <= n; i++)
		{
			operationSet[index] = i;
			get_all_operations(n, index + 1);
			operationSet[index] = 0;
		}

}

void get_operation_matrix(int operationSet[], int n)
{
	int j = 1;
	int k = 1;
	for (int i = 1; i <= n * n; i++)
	{
		
		operationMatrix[k][j] = operationSet[i];
		j++;
		if (j > n)
		{
			j = 1;
			k++;
		}
			

	}

	/*for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
			cout << operationMatrix[i][j] << " ";
		cout << endl;
	}

	cout << endl;*/
			
}	

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
