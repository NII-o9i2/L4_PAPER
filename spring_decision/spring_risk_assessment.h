/**************************
 * author: xiaotong.feng
 * 
 * For test self-driving  behavioral decision-making model 
 * 
 * ************************/

#pragma once

#include "data_type_test.h"


class SpringRiskAssess{
    public:
    SpringRiskAssess() = default;

    void SetKineticParameters(const EgoState& ego_state, const double lanewidth){
        // x,y means  lat,lon axis
        // vy = lon_velocity
        spring_a_ = ego_state.vy * 1.5;
        spring_b_ = lanewidth;
        lanewidth_ = lanewidth;
        x_ego_z1_ = x_ego_;
        y_ego_z1_ = y_ego_;
        x_ego_ = ego_state.x;
        y_ego_ = ego_state.y;
        // todo to judge vy or v
        v_i_ = ego_state.velocity;
        ego_yaw_ = ego_state.yaw;
    };
    
    void SetVehicleParameters(const EgoState& ego_state){ m_i_ = ego_state.mass; }

    void SetSL(const double s, const double l){ s_ = s; l_ =l;  }
    
    void SetTrafficParameters(const double velocity_limit,const double velocity_expect){ 
        v_limit_ = velocity_limit; 
        v_expect_  = velocity_expect;
    }
    
    const double CalculateCost(const Obstacle* obstacles);


    private:
        double spring_a_;
        double spring_b_;
        double v_limit_;
        double x_ego_;
        double y_ego_;
        double x_ego_z1_;
        double y_ego_z1_;
        double m_i_;
        double v_expect_;
        double lanewidth_;
        double v_i_;
        double s_;
        double l_;
        double ego_yaw_;
        // todo from hdmao , 3 for dotted line; 2 for solid line
        double line_type_ = 2.0;

}; // end class 