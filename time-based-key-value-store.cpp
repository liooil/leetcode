#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

// =============================================================================

struct TimeStrings {
    vector<int> time;
    vector<string> value;
    void set(int timestamp, string value) {
        this->time.push_back(timestamp);
        this->value.push_back(value);
    }
    string get(int timestamp) const {
        int lo = 0;
        int hi = time.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (timestamp < time[mid]) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        if (lo == 0) {
            return "";
        }
        return value[lo-1];
    }
};

class TimeMap {
public:
    /** Initialize your data structure here. */
    TimeMap() : m_timeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        if (m_timeMap.count(key) == 0) {
            m_timeMap[key] = TimeStrings();
        }
        m_timeMap[key].set(timestamp, value);
    }
    
    string get(string key, int timestamp) {
        if (m_timeMap.count(key) == 0) {
            return "";
        }
        return m_timeMap[key].get(timestamp);
    }
private:
    map<string, TimeStrings> m_timeMap;
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */

// =============================================================================

int main() {
    TimeMap tm = TimeMap();
    tm.set("foo","bar",1);
    cout << tm.get("foo",1);
    cout << tm.get("foo",3);
    tm.set("foo","bar2",4);
    cout << tm.get("foo",4);
    cout << tm.get("foo",5);
}