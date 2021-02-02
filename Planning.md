# PlanningBase

## Init

### PlanningContext->Init

### TaskFactory->Init

## Name

## RunOnce

## Plan

## FillPlanningPb

## Var

### local_view_

### hdmap_

### start_time_

### seq_num_

### config_

### traffic_rule_configs_

### frame_

### planner_

### last_publishable_trajectory_

### planner_dispatcher_

## FSM

### Planning Dispatcher

- Scenario handler Default
- Scenario handler STOP Sign
- Scenario handler Tracffic Light
- Scenario handler Bare Intersection
- Scenario handler Valet
- Scenario handler Pull Over

## Planning Context

## TrajectoryStitcher

### TransformLastPublishedTrajectory

### ComputeStitchingTrajectory

- stitch is disabled
- replan for no previous trajectory
- replan for manual mode
- replan for empty previous trajectory
- replan for time wrong
- replan for path point wrong
- replan for high diff

  lat：0.5
  lon：2.5

### ComputeReinitStitchingTrajectory

- Predict

	- RearCenteredKinematicBicycleModel

- ComputeTrajectoryPointFromVehicleState

### ComputePositionProjection

### ComputeTrajectoryPointFromVehicleState

## PlanningComponent

###  Init

-  choose planningbase

	- NaviPlanning
	- OnLanePlanning

- planning_base_->Init
- CreateReader

	- routing_reader_
	- traffic_light_reader_
	- pad_msg_reader_
	- relative_map_reader_ : FLAGS_use_navigation_mode

- CreateWriter

	- planning_writer_
	- rerouting_writer_

###  Proc

- CheckRerouting
- Creat input data: local_view

	- routing
	- traffic_light
	- pad_msg

- planning_base_->RunOnce
- FillHeader
- Modify set_relative_time
- planning_writer_

### CheckRerouting

### CheckInput

### Var

- traffic_light_reader_
- routing_reader_
- pad_msg_reader_
- relative_map_reader_
- planning_writer_
- rerouting_writer_
- mutex_
- traffic_light_
- routing_
- pad_msg_
- relative_map_
- local_view_
- planning_base_
- config_

## NaviPlanning

## OnLanePlanning

### OnLanePlanning

- planner_dispatcher_

### Name

### Init

- CheckPlanningConfig
- PlanningBase-> Init
- planner_dispatcher_->Init
- Get traffic_rule_config
- Clear

	- planning instance
	- planning status

- Load

	- hdmap_
	- reference_line_provider_
	- planner_

	  planner_ = planner_dispatcher_->DispatchPlanner()

	- start_time_

### RunOnce

- Get info 

	- localization
	- chassis

- VehicleStateProvider

	- Update
	- vehicle_state

- CheckFail

	- decision - > msg
	- set_gear
	- FillPlanningPb
	- GenerateStopTrajectory

- AlignTimeStamp

  timestamp t<0.02

-  Check :IsDifferentRouting

	- Update: reference_line_provider_

- ComputeStitchingTrajectory
- InitFrame

	- status.ok

		- CalculateFrontObstacleClearDistance

		  calculate front_clear_distance

		- RecordInputDebug

	- ! status.ok

		- Estop & Set gear

- TrafficDecider
- Plan

### Plan

- planer_ - > plan

### InitFrame

- frame_ -> reset
- reference_line_provider_->GetReferenceLines
- Get forward 8*speed & backward 50 meters
- frame_->Init

### AlignTimeStamp

- EstimateFuturePosition

  x = -v/angle_v*(1-cos(angle_v*t))+x
  y = v/angle_v*sin(angle_v*t)+y

### ExportReferenceLineDebug

### CheckPlanningConfig

### GenerateStopTrajectory : TODO

### ExportFailedLaneChangeSTChart

### ExportOnLaneChart

### ExportOpenSpaceChart

### AddOpenSpaceOptimizerResult

### AddPartitionedTrajectory

### AddStitchSpeedProfile

### AddPublishedSpeed

### AddPublishedAcceleration

### AddFallbackTrajectory

### Var

- last_routing_
- reference_line_provider_
- planning_smoother_

## 待完善

## 流程

## private

## public

## 变量

## TODO

## CLass

## TrafficDecider

### Init

### Execute

- check config 
- s_rule_factory.CreateObject
- rule->ApplyRule
- BuildPlanningTarget

### s_rule_factory

### RegisterRules

### BuildPlanningTarget

- StopPoint

	- Soft
	- Hard

- SetLatticeStopPoint

### rule_configs_

## Planer

### Name

### Init

### Plan

### Stop

### var

- config_
- scenario_manager_
- scenario_

## PlannerDispatcher

### Init

### DispatchPlanner

### RegisterPlanners

- RTKReplayPlanner
- PublicRoadPlanner
- LatticePlanner
- NaviPlanner

### planner_factory_

## PublicRoadPlanner

### Stop

### Name

### Init

### Plan

- scenario_manager_.Update
- scenario_ -> Process

	- xxx  Decider

- scenario_manager_.Update

## ScenarioManager

### Init

### mutable_scenario

### Update

-   Observe
- ScenarioDispatch

### Observe

- Find Overlap

  PNC_JUNCTION || SIGNAL || STOO_SIGN || YIELD_SIGN

### CreateScenario

### RegisterScenarios

### SelectBareIntersectionScenario

### SelectPullOverScenario

-   set config
-   calculate destance_to_dest

  50.0 > des > 10.0

- check pull over status

  des < 25.0 pull_over = false

- check around junction

  junction 前后8米不会pull over

- check rightmost lane type

  最右车道类型不为city_driving

### SelectPadMsgScenario

### SelectInterceptionScenario

- check  traffic sign  overlap & pnc_junction overlap
- if  tracffic sign first 

	- STOP_SIGN

		- PROTECTED
		- UNPROTECTED

	- SIGNAL

		- LEFT UNPROTECTED
		- RIGHT UNPROTECTED
		- PROTECTED

	- YIELD_SIGN

- if   PNC_junction first 

	- BareIntersection

### SelectStopSignScenario

### SelectTrafficLightScenario

### SelectValetParkingScenario

- IsTransferable

### SelectYieldSignScenario

### SelectParkAndGoScenario

- check  ego vehicle distance & destination

  vehicle speed && lane type && destination distance

### ScenarioDispatch

- scenario_type = defualt lane_follow
-   Observe
- SelectParkAndGoScenario
- SelectInterceptionScenario
- SelectPullOverScenario
- SelectValetParkingScenario

### IsBareIntersectionScenario

### IsStopSignScenario

### IsTrafficLightScenario

### IsYieldSignScenario

### UpdatePlanningContext

### UpdatePlanningContextBareIntersectionScenario

### UpdatePlanningContextEmergencyStopcenario

### UpdatePlanningContextPullOverScenario

### UpdatePlanningContextStopSignScenario

### UpdatePlanningContextTrafficLightScenario

### UpdatePlanningContextYieldSignScenario

### var

- config_map_
- current_scenario_
- default_scenario_type_
- scenario_context_
- first_encountered_overlap_map_

## PlannerWithReferenceLine

### PlanOnReferenceLine

## Stage

### StageStatus

- ERROE
- READY
- RUNNING
- FINISHED

### config

### stage_type

### Process

### TaskList

### Name

### GetContextAs

### SetContext

### FindTask

### NextStage

### ExecuteTaskOnReferenceLine

### ExecuteTaskOnOpenSpace

### FinishScenario

### VAR

- tasks_
- task_list_
- config_
- next_stage_
- context_
- name_

## LaneFollowStage

### Process

- PlanOnReferenceLine
- Check changeline

  reference_line_info.IsChangeLanePath()

	- PlanOnReferenceLine
	- PlanOnReferenceLine
	- PlanOnReferenceLine

### PlanOnReferenceLine

- reference_line_info->AddCost
- go through task_list_

	- LANE_CHANGE_DECIDER
	- PATH_REUSE_DECIDER
	- PATH_LANE_BORROW_DECIDER
	- PATH_BOUNDS_DECIDER
	- PIECEWISE_JERK_PATH_OPTIMIZER
	- PATH_ASSESSMENT_DECIDER
	- PATH_DECIDER
	- RULE_BASED_STOP_DECIDER
	- ST_BOUNDS_DECIDER
	- SPEED_BOUNDS_PRIORI_DECIDER
	- SPEED_HEURISTIC_OPTIMIZER
	- SPEED_DECIDER
	- SPEED_BOUNDS_FINAL_DECIDER
	- PIECEWISE_JERK_SPEED_OPTIMIZER
	- PIECEWISE_JERK_NONLINEAR_SPEED_OPTIMIZER
	- RSS_DECIDER

- Decider failed

	- PlanFallbackTrajectory

- search destination
- search obstacles

### PlanFallbackTrajectory

### GenerateFallbackPathProfile

### RetrieveLastFramePathProfile

### GetStopSL

### RecordObstacleDebugInfo

### VAR

- stage_

## LaneFollowScenario

### CreateStage

## Scenario

### StageStatus

- STATUS_UNKNOWN
- STATUS_PROCESSING
- STATUS_DONE

### LoadConfig

### scenario_type

### CreateStage

### IsTransferable

### Process

- Check NO_STAGE
- current_stage_->Process

	- ERROR
	- RUNNING
	- FINISHED

		- current_stage -> nextstage
		- current_stage_ -> STATUS_PROCESSING

### GetStatus

### GetStage

### Init

### Name

### GetMsg

### VAR

- scenario_status_
- current_stage_
- config_
- stage_config_map_
- scenario_context_
- name_
- msg_

## ReferenceLineInfo

### LaneType

- LeftForward
- LeftReverse
- RightForward
- RightReverse

### Init

### AddObstacles

### AddObstacle

### vehicle_state

### path_decision

### reference_line

### mutable_reference_line

### SDistanceToDestination

### ReachedDestination

### SetTrajectory

### trajectory

### Cost

### AddCost

### SetCost

### PriorityCost

### SetPriorityCost

### SetLatticeStopPoint

### SetLatticeCruiseSpeed

### planning_target

### SetCruiseSpeed

### GetCruiseSpeed

### LocateLaneInfo

### GetNeighborLaneInfo

### IsStartFrom

### mutable_debug

### debug

### mutable_latency_stats

### latency_stats

### path_data

### fallback_path_data

### speed_data

### mutable_path_data

### mutable_fallback_path_data

### mutable_speed_data

### rss_info

### mutable_rss_info

### CombinePathAndSpeedProfile

### AdjustTrajectoryWhichStartsFromCurrentPos

### AdcSlBoundary

### PathSpeedDebugString

### IsChangeLanePath

### IsNeighborLanePath

### SetDrivable

### IsDrivable

### ExportEngageAdvice

### Lanes

### TargetLaneId

### ExportDecision

### SetJunctionRightOfWay

### GetRightOfWayStatus

### GetPathTurnType

### GetIntersectionRightofWayStatus

### OffsetToOtherReferenceLine

### SetOffsetToOtherReferenceLine

### GetCandidatePathBoundaries

### SetCandidatePathBoundaries

### GetCandidatePathData

### SetCandidatePathData

### GetBlockingObstacle

### SetBlockingObstacle

### is_path_lane_borrow

### set_is_path_lane_borrow

### set_is_on_reference_line

### GetPriority

### SetPriority

### set_trajectory_type

### trajectory_type

### mutable_st_graph_data

### st_graph_data

### OverlapType

- CLEAR_AREA
- CROSSWALK
- OBSTACLE
- PNC_JUNCTION
- SIGNAL
- STOP_SIGN
- YIELD_SIGN

### FirstEncounteredOverlaps

### GetPnCJunction

### GetAllStopDecisionSLPoint

### SetTurnSignal

### SetEmergencyLight

### set_path_reusable

### path_reusable

### InitFirstOverlaps

### CheckChangeLane

### SetTurnSignalBasedOnLaneTurnType

### ExportVehicleSignal

### IsIrrelevantObstacle

### MakeDecision

### MakeMainStopDecision

### MakeMainMissionCompleteDecision

### MakeEStopDecision

### SetObjectDecisions

### AddObstacleHelper

### GetFirstOverlap

### Var

- junction_right_of_way_map_
- vehicle_state_
- adc_planning_point_
- reference_line_
- cost_
- is_drivable_
- path_decision_
- blocking_obstacle_
- candidate_path_boundaries_
- candidate_path_data_
- path_data_
- fallback_path_data_
- speed_data_
- discretized_trajectory_
- rss_info_
- adc_sl_boundary_
- debug_
- latency_stats_
- lanes_
- is_on_reference_line_
- is_path_lane_borrow_
- status_
- offset_to_other_reference_line_
- priority_cost_
- planning_target_
- trajectory_type_
- first_encounter_overlaps_
- st_graph_data_
- vehicle_signal_
- cruise_speed_
- path_reusable_

## Frame

### PlanningStartPoint

### Init

### InitForOpenSpace

### SequenceNum

### DebugString

### ComputedTrajectory

### RecordInputDebug

### reference_line_info

### mutable_reference_line_info

### Find

### FindDriveReferenceLineInfo

### FindTargetReferenceLineInfo

### FindFailedReferenceLineInfo

### DriveReferenceLineInfo

### obstacles

### CreateStopObstacle

### CreateStaticObstacle

### Rerouting

### vehicle_state

### AlignPredictionTime

### set_current_frame_planned_trajectory

### current_frame_planned_trajectory

### set_current_frame_planned_path

### current_frame_planned_path

### is_near_destination

### UpdateReferenceLinePriority

### local_view

### GetObstacleList

### open_space_info

### mutable_open_space_info

### GetSignal

### GetPadMsgDrivingAction

### InitFrameData

### CreateReferenceLineInfo

### FindCollisionObstacle

### CreateStaticVirtualObstacle

### AddObstacle

### ReadTrafficLights

### ReadPadMsgDrivingAction

### ResetPadMsgDrivingAction

### Var

- pad_msg_driving_action_
- sequence_num_
- local_view_
- hdmap_
- planning_start_point_
- vehicle_state_
- reference_line_info_
- is_near_destination_
- drive_reference_line_info_
- obstacles_
- traffic_lights_
- current_frame_planned_trajectory_
- current_frame_planned_path_
- reference_line_provider_
- open_space_info_
- future_route_waypoints_
- monitor_logger_buffer_

*XMind - Trial Version*