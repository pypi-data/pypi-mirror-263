from .scheduler_type import WonderSchedulerType

from diffusers import (
    DDIMScheduler,
    DDPMScheduler,
    DEISMultistepScheduler,
    DPMSolverMultistepScheduler,
    DPMSolverSinglestepScheduler,
    EulerAncestralDiscreteScheduler,
    EulerDiscreteScheduler,
    HeunDiscreteScheduler,
    KDPM2AncestralDiscreteScheduler,
    KDPM2DiscreteScheduler,
    LMSDiscreteScheduler,
    PNDMScheduler,
    UniPCMultistepScheduler)



SCHEDULER_MAP = {
    WonderSchedulerType.DDIM: lambda config: DDIMScheduler.from_config(config),
    WonderSchedulerType.DDPM: lambda config: DDPMScheduler.from_config(config),
    WonderSchedulerType.DEIS_MULTISTEP: lambda config: DEISMultistepScheduler.from_config(config),
    WonderSchedulerType.DPM_SOLVER_MULTISTEP: lambda config: DPMSolverMultistepScheduler.from_config(config),
    WonderSchedulerType.DPM_SOLVER_MULTISTEP_2M_KARRAS: lambda config: DPMSolverMultistepScheduler.from_config(config, use_karras_sigmas=True),
    WonderSchedulerType.DPM_SOLVER_MULTISTEP_2M_SDE: lambda config: DPMSolverMultistepScheduler.from_config(config, algorithm_type='sde-dpmsolver++'),
    WonderSchedulerType.DPM_SOLVER_MULTISTEP_2M_SDE_KARRAS: lambda config: DPMSolverMultistepScheduler.from_config(config, use_karras_sigmas=True, algorithm_type='sde-dpmsolver++'),
    WonderSchedulerType.DPM_SOLVER_SINGLESTEP: lambda config: DPMSolverSinglestepScheduler.from_config(config),
    WonderSchedulerType.DPM_SOLVER_SINGLESTEP_KARRAS: lambda config: DPMSolverSinglestepScheduler.from_config(config, use_karras_sigmas=True),
    WonderSchedulerType.EULER_ANCESTRAL_DISCRETE: lambda config: EulerAncestralDiscreteScheduler.from_config(config),
    WonderSchedulerType.EULER_DISCRETE: lambda config: EulerDiscreteScheduler.from_config(config),
    WonderSchedulerType.HEUN_DISCRETE: lambda config: HeunDiscreteScheduler.from_config(config),
    WonderSchedulerType.KDPM2_ANCESTRAL_DISCRETE: lambda config: KDPM2AncestralDiscreteScheduler.from_config(config),
    WonderSchedulerType.KDPM2_ANCESTRAL_DISCRETE_KARRAS: lambda config: KDPM2AncestralDiscreteScheduler.from_config(config, use_karras_sigmas=True),
    WonderSchedulerType.KDPM2_DISCRETE: lambda config: KDPM2DiscreteScheduler.from_config(config),
    WonderSchedulerType.KDPM2_DISCRETE_KARRAS: lambda config: KDPM2DiscreteScheduler.from_config(config, use_karras_sigmas=True),
    WonderSchedulerType.LMS_DISCRETE: lambda config: LMSDiscreteScheduler.from_config(config),
    WonderSchedulerType.LMS_DISCRETE_KARRAS: lambda config: LMSDiscreteScheduler.from_config(config, use_karras_sigmas=True),
    WonderSchedulerType.PNDM: lambda config: PNDMScheduler.from_config(config),
    WonderSchedulerType.UNI_PC_MULTISTEP: lambda config: UniPCMultistepScheduler.from_config(config),
}
