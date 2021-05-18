/**************************
 * author: NII-o9i2
 * 
 * For test self-driving  behavioral decision-making model 
 * 
 * ************************/

#pragma once

#include "data_list.h"
#include <math.h>

class SpringRiskAssess{
    public:
    SpringRiskAssess() = default;

    explicit SetKineticParameters(const EgoState& ego_state, const double lanewidth){
        // x,y means  lat,lon axis
        // vy = lon_velocity
        spring_a_ = ego_state.vy * 1.5;
        spring_b_ = lanewidth;
        lanewidth_ = lanewidth;
        x_ego_ = ego_state.x;
        y_ego_ = ego_state.y;
        m_i_ = ego_state.mass;
        // todo to judge vy or v
        v_i_ = ego_state.velocity;
    };
    
    explicit SetSL(const double s, const double l){ s_ = s; l_ =l;  }
    
    explicit SetTrafficParameters(const double velocity_limit,const double velocity_expect){ 
        v_limit_ = velocity_limit; 
        v_expect_  = velocity_expect;

    }
    
    explicit CalculateCost(const Obstacle* obstacles,){
        double g_i = 0.0;
        double k_g = 0.2;
        double tao = 1.0;
        double tao2 = 1.2;
        // G_i = m_i * g_h = m_i * k * v_der / v_limit * g
        g_i = m_i_ * k_g * v_expect_ / v_limit_ * 9.8;
        double f_di = g_i * pow(v_i_/v_limit_,tao);
        double f_li = 1.5 * m_i_ * line_type_ * pow(lanewidth_/2.0 - abs(l_),tao2);
        double t = 0.5 * m_i_ * v_i_ * v_i_;
        
        //calculate spring model

    }






    private:
        double spring_a_;
        double spring_b_;
        double v_limit_;
        double x_ego_;
        double y_ego_;
        double m_i_;
        double v_expect_;
        double lanewidth_;
        double v_i_;
        double s_;
        double l_;
        // todo from hdmao , 3 for dotted line; 2 for solid line
        double line_type_ = 2.0;



}