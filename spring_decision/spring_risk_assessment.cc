/**************************
 * author: xiaotong.feng
 * 
 * For test self-driving  behavioral decision-making model 
 * 
 * ************************/

#include "spring_risk_assessment.h"

#include <math.h>

const double SpringRiskAssess::CalculateCost(const Obstacle* obstacles){
        double g_i = 0.0;
        double k_g = 0.2;
        double tao = 1.0;
        double tao2 = 1.2;
        double f_ij = 0.0;
        double theta;
        // G_i = m_i * g_h = m_i * k * v_der / v_limit * g
        g_i = m_i_ * k_g * v_expect_ / v_limit_ * 9.8;
        double f_di = g_i * pow(v_i_/v_limit_,tao);
        double f_li = 1.5 * m_i_ * line_type_ * pow(lanewidth_/2.0 - abs(l_),tao2);
        double t = 0.5 * m_i_ * v_i_ * v_i_;
        
        /*
        obstacle struct 
        -mass 
        -x
        -y
        -velocity
        -valid
        */

        // calculate spring parameters
        double k_j_2 = 0.0;
        double d_i_j = 0.0;
        double delta_x_i_j = 0.0;
        double obstacle_sum_x = 0.0;
        double obstacle_sum_y = 0.0;

        obstacle_sum_x = - g_i + f_di;
        obstacle_sum_y = f_li;

        for(int i = 1; i < 32; i++){
            if (!obstacles[i].valid){
                continue;
            }else{
        // calculate obstacles distance
            d_i_j = sqrt((x_ego_ - obstacles[i].x)*(x_ego_ - obstacles[i].x) + (y_ego_ - obstacles[i].y)*(y_ego_ - obstacles[i].y));
        // calculate obstacles stiffness            
        // todo need to verify  (4 * spring_a_ * d_i_j) or (2 * d_i_j)
            k_j_2 = obstacles[i].mass * obstacles[i].velocity * obstacles[i].velocity / ( 4 * spring_a_ * d_i_j);
        // calculate delta x_ij
            delta_x_i_j = sqrt(spring_a_ * spring_a_ * (x_ego_ - obstacles[i].x)*(x_ego_ - obstacles[i].x)  + spring_b_ * spring_b_ * (y_ego_ - obstacles[i].y)*(y_ego_ - obstacles[i].y));
            delta_x_i_j = delta_x_i_j / d_i_j - d_i_j;

        if (delta_x_i_j > 0){
            f_ij = k_j_2 * delta_x_i_j;
            theta = atan2(obstacles[i].y - y_ego_,obstacles[i].x - x_ego_) - ego_yaw_;
        }else{
            f_ij = 0.0;
        }
            obstacle_sum_x += f_ij*cos(theta);
            obstacle_sum_y += f_ij*sin(theta);
        }//end if valid
        }//end for
        double u = 0.1;
        u = obstacle_sum_x * (x_ego_ - x_ego_z1_) + obstacle_sum_y * (y_ego_ - y_ego_z1_); 
        return u;
}
//calculate spring model

