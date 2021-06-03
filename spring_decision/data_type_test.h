/**************************
 * author: xiaotong.feng
 * 
 * For test data input & output
 * 
 * ************************/

#pragma once
#include <string>
#include <vector>
#include <iostream>
#include "jsoncpp/dist/json/json.h"
#include "fstream"
#include "assert.h"


class data_type_test
{
private:
    std::string filename_;
    Json::Value rqt_;
    std::vector<EgoState> ego_states_;
    std::ifstream ifs_;
public:
    data_type_test() = default;
    ~data_type_test() = default;

    // set test case name
    data_type_test(std::string name){
        filename_ = name;
        ifs_.open(name);
        assert(ifs_.is_open());
    };

    const std::string name() { return filename_; };
    
    // get the test data
    bool CatchTestData(){
        Json::Reader reader;
        if (!reader.parse(ifs_,rqt_,false)){
            std::cout<<"Data Error!"<<std::endl;
            return false;
        }
        return true;
    };


};

struct  EgoState
{
    double x;
    double y;
    double vx;
    double vy;
    double velocity;
    double yaw;
    double mass;
};
    /*
    obstacle struct 
    -mass 
    -x
    -y
    -velocity
    -valid
    */
struct  Obstacle
{
    double mass;
    double x;
    double y;
    double velocity;
    bool valid;

};
