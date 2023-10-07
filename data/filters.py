from .common import Service

def filter_cloud_provider(provider: str):
  def fn(seq: Service, provider: str):
    if seq.provider.name.lower() == provider.lower():
      return True
    else:
      return False

  return list(
    filter(
        lambda seq: fn(seq, provider), 
        Service.instances
    )
)



