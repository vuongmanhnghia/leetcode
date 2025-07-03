#include <cstddef>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    vector<int> target_indices;

    unordered_map<int, int> hash_table;

    for (size_t i = 0; i < nums.size(); i++) {
      int second_integer = target - nums.at(i);

      if (hash_table.find(second_integer) != hash_table.end()) {
        target_indices.push_back(i);
        target_indices.push_back(hash_table.find(second_integer)->second);
        break;
      } else {
        hash_table[nums.at(i)] = i;
      }
    }

    return target_indices;
  }
};
int main(int argc, char *argv[]) {
  vector<int> nums;

  cout << "Size vector: ";
  int size;
  cin >> size;

  for (int i = 0; i < size; i++) {
    int x;
    cout << "Number " << i << ": ";
    cin >> x;
    nums.push_back(x);
  }
  int target;
  cout << "Target number: ";
  cin >> target;

  Solution solution;
  vector<int> result = solution.twoSum(nums, target);

  cout << "Result: " << endl;
  for (int x : result) {
    cout << x << " ";
  }
  return 0;
}
