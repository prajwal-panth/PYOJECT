/*
If scanf reads a string from the input and stores it in the expr buffer. It will
read up to 99 characters, ensuring that the buffer (MaxExprLength 100) does not overflow.
The checkInp is checked to see if it is equal to 1.
If scanf successfully reads one string, it returns 1. If it encounters an error
or reaches the end of input without successfully reading a string, it returns a
different value (usually 0 or EOF).
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "decoration.h"

#define MaxExprLength 100
#define ErrDivisionByZero -1
#define ErrInvalidExpression -2

char expr[MaxExprLength];
int error = 0;

int IsDigit(char ch); // Helper Function

// every Validate function returns 0 for valid condition
int ValidateBrackets();
int ValidateSymbols();
int ValidateFloat();
int ValidateOperands();

double EvaluateSimpleExpression();
double EvaluateExpression();
double PerformOperation(double firstNum, double secondNum, char operator);

int main()
{
    color_box();
    calc_ascii();
    printf("%s %s %s\n", Blue, __DATE__, Reset);
    printf("%s %s %s\n", Blue, __TIME__, Reset);
    while (1)
    {
        printf("%sEnter your expression (or 'q' to quit):%s ", Pink, Reset);

        int checkInp = scanf("%99s", expr);

        if (checkInp != 1)
        {
            printf("%sError reading input. Please try again.%s\n", Red, Reset);
            continue;
        }

        if (strcmp(expr, "q") == 0)
        {
            printf("%s\nProgram Exited %s\n", Red, Reset);
            break;
        }

        if (ValidateBrackets() != 0)
        {
            printf("%sError: Mismatched brackets%s\n", Red, Reset);
            continue;
        }

        if (ValidateSymbols() != 0)
        {
            printf("%sError: Invalid symbols in expression%s\n", Red, Reset);
            continue;
        }

        if (ValidateFloat() != 0)
        {
            printf("%sError: Invalid floating point number%s\n", Red, Reset);
            continue;
        }

        if (ValidateOperands() != 0)
        {
            printf("%sError: Invalid expression - missing operator between operands%s\n", Red, Reset);
            continue;
        }

        error = 0;
        double result = EvaluateExpression();
        if (error == ErrDivisionByZero)
        {
            printf("%sError: Division by zero%s\n", Red, Reset);
        }
        else if (error == ErrInvalidExpression)
        {
            printf("%sError: Invalid expression%s\n", Red, Reset);
        }
        else
        {
            printf("%sResult: %.6f %s\n", BrightCyan, result, Reset);
        }
    }

    return 0;
}

int IsDigit(char ch)
{
    return ch >= '0' && ch <= '9';
}

int ValidateBrackets()
{
    int count = 0;
    for (int i = 0; expr[i]; i++)
    {
        if (expr[i] == '(')
            count++;
        if (expr[i] == ')')
            count--;
        if (count < 0)
            return -1;
    }
    return count == 0 ? 0 : -1;
}

int ValidateSymbols()
{
    const char *validChars = "0123456789.+-*/%^() ";
    for (int i = 0; expr[i]; i++)
    {
        if (strchr(validChars, expr[i]) == NULL)
        {
            return -1;
        }
    }
    return 0;
}

int ValidateFloat()
{
    for (int i = 0; expr[i]; i++)
    {
        if (expr[i] == '.')
        {
            i++; // Move to the next character
            if (!IsDigit(expr[i]))
            {
                return -1; // No digit found after the dot, invalid floating point number
            }
            while (IsDigit(expr[i]))
            {
                i++;
            }
            if (expr[i] == '.')
            {
                return -1; // Multiple dots found, invalid floating point number
            }
            i--; // Move back one as the main loop will increment
        }
    }
    return 0;
}

int ValidateOperands()
{
    int needOperand = 1; // We need an operand at the start
    int lastWasNumber = 0;

    for (int i = 0; expr[i]; i++)
    {
        if (IsDigit(expr[i]) || expr[i] == '.')
        {
            lastWasNumber = 1;
            needOperand = 0;
        }
        else if (expr[i] == '(')
        {
            if (!needOperand && lastWasNumber)
            {
                return -1; // Invalid: number immediately before opening bracket
            }
            needOperand = 1;
        }
        else if (expr[i] == ')')
        {
            if (needOperand)
            {
                return -1; // Invalid: closing bracket where we need an operand
            }
        }
        else if (strchr("+-*/%^", expr[i]))
        {
            if (needOperand)
            {
                return -1; // Invalid: operator where we need an operand
            }
            needOperand = 1;
            lastWasNumber = 0;
        }
        else if (expr[i] != ' ')
        {
            return -1; // Invalid character
        }
    }

    if (needOperand)
    {
        return -1; // Invalid: expression ends with an operator
    }
    return 0; // All operands are valid
}

double PerformOperation(double firstNum, double secondNum, char operator)
{
    switch (operator)
    {
    case '+':
        return firstNum + secondNum;
    case '-':
        return firstNum - secondNum;
    case '*':
        return firstNum * secondNum;
    case '/':
        if (secondNum == 0)
        {
            error = ErrDivisionByZero;
            return 0;
        }
        return firstNum / secondNum;
    case '%':
        if (secondNum == 0)
        {
            error = ErrDivisionByZero;
            return 0;
        }
        return fmod(firstNum, secondNum);
    case '^':
        return pow(firstNum, secondNum);
    default:
        return secondNum; // For the first number in the expression
    }
}

double EvaluateSimpleExpression()
{
    double result = 0;
    double currentNum = 0;
    char currentOp = '+';

    for (int i = 0; expr[i]; i++)
    {
        if (IsDigit(expr[i]) || expr[i] == '.')
        {
            currentNum = atof(expr + i);
            while (IsDigit(expr[i]) || expr[i] == '.')
                i++;
            i--; // Move back one character as the main loop will increment
        }
        else if (strchr("+-*/%^", expr[i]))
        {
            result = PerformOperation(result, currentNum, currentOp);
            if (error != 0)
                return 0;
            currentNum = 0;
            currentOp = expr[i];
        }
        else if (expr[i] != ' ')
        {
            error = ErrInvalidExpression;
            return 0;
        }
    }

    result = PerformOperation(result, currentNum, currentOp);
    return result;
}

double EvaluateExpression()
{
    double result = 0;
    char subExpr[MaxExprLength] = "";
    int subExprIndex = 0;
    int bracketDepth = 0;

    for (int i = 0; expr[i]; i++)
    {
        if (expr[i] == '(')
        {
            bracketDepth++;
            continue;
        }

        if (expr[i] == ')')
        {
            bracketDepth--;
            if (bracketDepth == 0)
            {
                subExpr[subExprIndex] = '\0';
                strcpy(expr, subExpr);
                result = EvaluateSimpleExpression();
                if (error != 0)
                    return 0;
                subExprIndex = 0;
                continue;
            }
        }

        if (bracketDepth > 0)
        {
            subExpr[subExprIndex++] = expr[i];
        }
        else
        {
            subExpr[subExprIndex++] = expr[i];
            if (expr[i + 1] == '\0' || expr[i + 1] == '(')
            {
                subExpr[subExprIndex] = '\0';
                strcpy(expr, subExpr);
                result = EvaluateSimpleExpression();
                if (error != 0)
                    return 0;
                subExprIndex = 0;
            }
        }
    }

    return result;
}