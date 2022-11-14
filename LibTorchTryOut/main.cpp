/**
 * This is sample LibTorch tryout.
 */
#include <iostream>
#include <torch/torch.h>
using namespace std;
int main()
{
	cout<<"This is a test"<<endl;
    // A random 3 x 3 tensor in CPU
	torch::Tensor x = torch::randn({3,3});
	cout<<x<<endl;

	// A random 3 x 3 tensor in GPU
	torch::Tensor y = torch::randn({3,3}, torch::kCUDA);
	cout<<y<<endl;

	return 0;

}
