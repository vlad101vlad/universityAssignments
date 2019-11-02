// project4_1stTry.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>

using namespace std;

ofstream fout("test7.out");

int set[10]; // This is the initial set with n_elements
int operation_matrix[10][10]; // This is the operation matrix which will contain 
int n_elements;
int counter = 0; // This counter will count how many elements we have populated the operation_matrix with
int matrices_number; // This counter keeps track of how many matrices we have generated for a set with n_elements

void populate_set();	// This function populates the set with n_elements
void insert_identity_element(int n); // This function initialisises the operation_matrix with the identity element
void print_operation_matrix(); // This function prints the operation_matrix 
void generate_operation_table(int, int);	// This is the backtracking function , it generates all the possible operation table for a function
int check_if_unique(int, int, int); // This function checks whether an element is unique in a line or in a row in the operation_matrix
void empty_operation_matrix(); /// This function sets all the elements of the operation_matrix to 0
bool check_if_associative();

int main()
{
	cout << "Enter number of elements: ";
	cin >> n_elements;
	populate_set();
	

	for (int i = 1; i <= n_elements; i++)
	{
		insert_identity_element(i);
		fout << "The abelian group structures on G with identity element [a" << i << "] are given by the matrices : " << endl;
		generate_operation_table(counter, i);
		empty_operation_matrix();
		counter = 0;

	}

	fout << "The number of abelian group structures on a set G = {";

	for (int i = 1; i <= n_elements; i++)
	{
		fout << "a" << i;
		if (i != n_elements)
			fout << ", ";

	}

	fout << "} is: " << matrices_number << endl;


}

void populate_set()
{
	for (int i = 1; i <= n_elements; i++)
		set[i] = i;
}

void insert_identity_element(int n)
{
	for (int i = 1; i <= n_elements; i++)
	{
		counter += 2;
		operation_matrix[n][i] = operation_matrix[i][n] = i;
	}
	counter--;
		
}

void print_operation_matrix()
{
	for (int i = 1; i <= n_elements; i++)
	{
		for (int j = 1; j <= n_elements; j++)
			fout << "a" << operation_matrix[i][j] << " ";
		fout << endl;
	}
}

void generate_operation_table(int index, int identity_element)
{	
	

	if (index == n_elements*n_elements)
	{
		if(check_if_associative())
		{
			matrices_number++;
			print_operation_matrix();
			fout << endl;
		}
		
	}		
	else
	{
		for(int i = 1; i <= n_elements; i++)
			for (int j = 1; j <= i; j++)
			{
				if (operation_matrix[i][j] == 0)
				{
					
					for(int k = 1; k <= n_elements; k++)
						if (i == j)
						{
							if (check_if_unique(k, j, i))
							{
								operation_matrix[i][j] = k;							
								generate_operation_table(index + 1, identity_element);								
								operation_matrix[i][j] = 0;
							}
						}
						else
						{
							if (check_if_unique(k, j, i) && check_if_unique(k, i, j))
							{
								operation_matrix[i][j] = k;
								operation_matrix[j][i] = k;																		
								generate_operation_table(index + 2, identity_element);								
								operation_matrix[i][j] = 0;
								operation_matrix[j][i] = 0;
							}
						}
					if (operation_matrix[i][j] == 0)
						return;
				}
							
				
			}
					

	}

}

int check_if_unique(int element, int line, int row)
{
	// check for line
	int ok = 1;
	for (int i = 1; i <= n_elements; i++)
		if (operation_matrix[row][i] == element || operation_matrix[i][line] == element)
			ok = 0;
	return ok;
	
}

void empty_operation_matrix()
{
	for (int i = 1; i <= n_elements; i++)
		for (int j = 1; j <= n_elements; j++)
			operation_matrix[i][j] = 0;
}


bool check_if_associative()
{
	for (int i = 1; i <= n_elements; i++)
		for (int j = 1; j <= n_elements; j++)
			for (int k = 1; k <= n_elements; k++)
				if (operation_matrix[operation_matrix[i][j]][k] != operation_matrix[i][operation_matrix[j][k]])
					return false;
	return true;
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
