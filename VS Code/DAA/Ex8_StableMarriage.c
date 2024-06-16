#include <stdio.h>

#define N 4 // Number of pairs 

int isStable(int prefer[2*N][N], int wPartner[], int m, int w)
{
    int i;
    for (i = 0; i < N; i++)
    {
        if (prefer[w+N][i] == m)
            return 0;
        if (prefer[w+N][i] == wPartner[w])
            return 1;
    }
}

void stableMarriage(int prefer[2*N][N])
{
    int wPartner[N]; 
    int mFree[N];    
    int i, m, w, m1;

    for (i = 0; i < N; i++)
    {
        wPartner[i] = -1;
        mFree[i] = 0;
    }

    int freeCount = N;
    while (freeCount > 0)
    {
        for (m = 0; m < N; m++)
            if (mFree[m] == 0)
                break;

        for (i = 0; i < N && mFree[m] == 0; i++)
        {
            w = prefer[m][i];

            if (wPartner[w - N] == -1)
            {
                wPartner[w - N] = m;
                mFree[m] = 1;
                freeCount--;
            }
            else 
            {
                m1 = wPartner[w - N];
                if (!isStable(prefer, wPartner, m, w))
                {
                    wPartner[w - N] = m;
                    mFree[m] = 1;
                    mFree[m1] = 0;
                }
            } 
        }     
    }       

    printf("Woman Man\n");
    for (i = 0; i < N; i++)
        printf(" %d \t %d\n", i + N, wPartner[i] + 1);
}

int main()
{
    int prefer[2*N][N] = {{7, 5, 6, 4},
                          {5, 4, 6, 7},
                          {4, 5, 6, 7},
                          {4, 5, 6, 7},
                          {0, 1, 2, 3},
                          {0, 1, 2, 3},
                          {0, 1, 2, 3},
                          {0, 1, 2, 3}};

    stableMarriage(prefer);
    return 0;
}
