# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prodvana/workflow/workflow_manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from prodvana.proto.prodvana.common_config import program_pb2 as prodvana_dot_common__config_dot_program__pb2
from prodvana.proto.prodvana.common_config import env_pb2 as prodvana_dot_common__config_dot_env__pb2
from prodvana.proto.validate import validate_pb2 as validate_dot_validate__pb2
from prodvana.proto.prodvana.repo import repo_pb2 as prodvana_dot_repo_dot_repo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(prodvana/workflow/workflow_manager.proto\x12\x11prodvana.workflow\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a$prodvana/common_config/program.proto\x1a prodvana/common_config/env.proto\x1a\x17validate/validate.proto\x1a\x18prodvana/repo/repo.proto\"\x92\x01\n\x16TrackedImageRepository\x12\x12\n\nrepository\x18\x01 \x01(\t\x12.\n\nlast_index\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x0cindex_status\x18\x03 \x01(\x0e\x32\x1e.prodvana.workflow.IndexStatus\"\x97\x01\n\rRegistryImage\x12+\n\x07\x63reated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0b\n\x03tag\x18\x05 \x01(\t\x12%\n\x06\x63ommit\x18\x06 \x01(\x0b\x32\x15.prodvana.repo.CommitJ\x04\x08\x01\x10\x02J\x04\x08\x04\x10\x05R\x06\x64igestR\x04tags\"e\n\x12ListRepoCommitsReq\x12\x12\n\nrepository\x18\x01 \x01(\t\x12\x14\n\x0cstarting_ref\x18\x02 \x01(\t\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\"V\n\x13ListRepoCommitsResp\x12&\n\x07\x63ommits\x18\x01 \x03(\x0b\x32\x15.prodvana.repo.Commit\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x94\x04\n%CreateContainerRegistryIntegrationReq\x12\x39\n\x04name\x18\x06 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^[a-z]([a-z0-9-]*[a-z0-9]){0,1}$\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0e\n\x06secret\x18\x03 \x01(\t\x12-\n\x04type\x18\x04 \x01(\x0e\x32\x1f.prodvana.workflow.RegistryType\x12Z\n\x0b\x65\x63r_options\x18\x05 \x01(\x0b\x32\x43.prodvana.workflow.CreateContainerRegistryIntegrationReq.ECROptionsH\x00\x12q\n\x17public_registry_options\x18\x07 \x01(\x0b\x32N.prodvana.workflow.CreateContainerRegistryIntegrationReq.PublicRegistryOptionsH\x00\x1aV\n\nECROptions\x12\x12\n\naccess_key\x18\x01 \x01(\t\x12\x12\n\nsecret_key\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x10\n\x08role_arn\x18\x04 \x01(\t\x1a\x17\n\x15PublicRegistryOptionsB\x12\n\x10registry_options\"?\n%CreateContainerRegistryIntegrationRes\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\">\n%DeleteContainerRegistryIntegrationReq\x12\x15\n\rregistry_name\x18\x01 \x01(\t\"(\n&DeleteContainerRegistryIntegrationResp\"<\n$ListContainerRegistryIntegrationsReq\x12\x14\n\x0c\x66\x65tch_status\x18\x01 \x01(\x08\"\xcc\x02\n\x1c\x43ontainerRegistryIntegration\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x31\n\x06status\x18\x05 \x01(\x0e\x32!.prodvana.workflow.RegistryStatus\x12K\n\x08\x65\x63r_info\x18\x06 \x01(\x0b\x32\x37.prodvana.workflow.ContainerRegistryIntegration.ECRInfoH\x00\x12?\n\x0crepositories\x18\x07 \x03(\x0b\x32).prodvana.workflow.TrackedImageRepository\x1a\x19\n\x07\x45\x43RInfo\x12\x0e\n\x06region\x18\x01 \x01(\tB\x0f\n\rregistry_info\"\xe0\x03\n%ListContainerRegistryIntegrationsResp\x12w\n\x14\x63ontainer_registries\x18\x01 \x03(\x0b\x32Y.prodvana.workflow.ListContainerRegistryIntegrationsResp.ContainerRegistryIntegrationInfo\x1a\x19\n\x07\x45\x43RInfo\x12\x0e\n\x06region\x18\x01 \x01(\t\x1a\xa2\x02\n ContainerRegistryIntegrationInfo\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x31\n\x06status\x18\x06 \x01(\x0e\x32!.prodvana.workflow.RegistryStatus\x12T\n\x08\x65\x63r_info\x18\x07 \x01(\x0b\x32@.prodvana.workflow.ListContainerRegistryIntegrationsResp.ECRInfoH\x00\x42\x0f\n\rregistry_infoJ\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05R\x08usernameR\rmasked_secret\";\n\"GetContainerRegistryIntegrationReq\x12\x15\n\rregistry_name\x18\x01 \x01(\t\"h\n#GetContainerRegistryIntegrationResp\x12\x41\n\x08registry\x18\x01 \x01(\x0b\x32/.prodvana.workflow.ContainerRegistryIntegration\"\x95\x01\n\x1dGetContainerRegistryImagesReq\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\x12\x18\n\x10image_repository\x18\x02 \x01(\t\x12\x1b\n\x13skip_registry_cache\x18\x03 \x01(\x08\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05\"j\n\x1dGetContainerRegistryImagesRes\x12\x30\n\x06images\x18\x01 \x03(\x0b\x32 .prodvana.workflow.RegistryImage\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"9\n\x1fListTrackedImageRepositoriesReq\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\"c\n ListTrackedImageRepositoriesResp\x12?\n\x0crepositories\x18\x01 \x03(\x0b\x32).prodvana.workflow.TrackedImageRepository\"J\n\x1cGetTrackedImageRepositoryReq\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\x12\x12\n\nrepository\x18\x02 \x01(\t\"^\n\x1dGetTrackedImageRepositoryResp\x12=\n\nrepository\x18\x01 \x01(\x0b\x32).prodvana.workflow.TrackedImageRepository\"I\n\x19TrackImageRepositoriesReq\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\x12\x14\n\x0crepositories\x18\x02 \x03(\t\"\x1c\n\x1aTrackImageRepositoriesResp\"L\n\x1eStopTrackingImageRepositoryReq\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\x12\x12\n\nrepository\x18\x02 \x01(\t\"!\n\x1fStopTrackingImageRepositoryResp\"u\n\x15GetImageCommitInfoReq\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\x12\x12\n\nrepository\x18\x02 \x01(\t\x12\r\n\x03tag\x18\x03 \x01(\tH\x00\x12\x0f\n\x05image\x18\x04 \x01(\tH\x00\x42\x10\n\x0eimage_id_oneof\"S\n\x16GetImageCommitInfoResp\x12%\n\x06\x63ommit\x18\x01 \x01(\x0b\x32\x15.prodvana.repo.Commit\x12\x12\n\nrepository\x18\x02 \x01(\t\"J\n\x10GetCommitInfoReq\x12\x1b\n\nrepository\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x19\n\x08\x63ommitId\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\":\n\x11GetCommitInfoResp\x12%\n\x06\x63ommit\x18\x01 \x01(\x0b\x32\x15.prodvana.repo.Commit\"\x92\x01\n\x15GetProgramDefaultsReq\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\x12\x12\n\nrepository\x18\x02 \x01(\t\x12\r\n\x03tag\x18\x03 \x01(\tH\x00\x12\x0f\n\x05image\x18\x04 \x01(\tH\x00\x12\x1b\n\x13skip_registry_cache\x18\x05 \x01(\x08\x42\x10\n\x0eimage_id_oneof\"\xed\x01\n\x0fProgramDefaults\x12\x0b\n\x03\x63md\x18\x01 \x03(\t\x12\x12\n\nentrypoint\x18\x02 \x03(\t\x12\x38\n\x03\x65nv\x18\x03 \x03(\x0b\x32+.prodvana.workflow.ProgramDefaults.EnvEntry\x12\x31\n\x05ports\x18\x04 \x03(\x0b\x32\".prodvana.common_config.PortConfig\x1aL\n\x08\x45nvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .prodvana.common_config.EnvValue:\x02\x38\x01\"V\n\x16GetProgramDefaultsResp\x12<\n\x10program_defaults\x18\x01 \x01(\x0b\x32\".prodvana.workflow.ProgramDefaults\"P\n\x16GetServiceImageInfoReq\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x10\n\x08versions\x18\x02 \x03(\t\x12\x13\n\x0b\x61pplication\x18\x03 \x01(\t\"\x98\x04\n\x17GetServiceImageInfoResp\x12\x12\n\nservice_id\x18\x01 \x01(\t\x12\x14\n\x0cservice_name\x18\x02 \x01(\t\x12M\n\rversion_infos\x18\x03 \x03(\x0b\x32\x36.prodvana.workflow.GetServiceImageInfoResp.VersionInfo\x1a\xc8\x01\n\x0bVersionInfo\x12\x0f\n\x07version\x18\x01 \x01(\t\x12M\n\rprogram_infos\x18\x02 \x03(\x0b\x32\x36.prodvana.workflow.GetServiceImageInfoResp.ProgramInfo\x12Y\n\x13per_release_channel\x18\x03 \x03(\x0b\x32<.prodvana.workflow.GetServiceImageInfoResp.PerReleaseChannel\x1a<\n\x0bProgramInfo\x12\x11\n\timage_url\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x03 \x03(\tJ\x04\x08\x02\x10\x03R\x06\x64igest\x1a{\n\x11PerReleaseChannel\x12\x17\n\x0frelease_channel\x18\x01 \x01(\t\x12M\n\rprogram_infos\x18\x02 \x03(\x0b\x32\x36.prodvana.workflow.GetServiceImageInfoResp.ProgramInfo\"D\n\x0fInstallSlackReq\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x14\n\x0credirect_uri\x18\x03 \x01(\t\"4\n\x10InstallSlackResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x17\n\x15GetInstallSlackUrlReq\"%\n\x16GetInstallSlackUrlResp\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x13\n\x11UninstallSlackReq\"%\n\x12UninstallSlackResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\"(\n\x0cSlackChannel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"H\n\x13InstallPagerDutyReq\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x14\n\x0credirect_uri\x18\x03 \x01(\t\"8\n\x14InstallPagerDutyResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1b\n\x19GetInstallPagerDutyUrlReq\")\n\x1aGetInstallPagerDutyUrlResp\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x17\n\x15UninstallPagerDutyReq\")\n\x16UninstallPagerDutyResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\",\n\x10PagerDutyService\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"E\n\x11InstallGrafanaReq\x12\x14\n\x03url\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x1a\n\tapi_token\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\",\n\x12InstallGrafanaResp\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\"\x15\n\x13UninstallGrafanaReq\".\n\x14UninstallGrafanaResp\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\"\x1b\n\x19GetGrafanaInstallationReq\"A\n\x1aGetGrafanaInstallationResp\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"\x1e\n\x1cListHoneycombEnvironmentsReq\"\xba\x01\n\x1dListHoneycombEnvironmentsResp\x12[\n\x0c\x65nvironments\x18\x01 \x03(\x0b\x32\x45.prodvana.workflow.ListHoneycombEnvironmentsResp.HoneycombEnvironment\x1a<\n\x14HoneycombEnvironment\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"M\n\x1a\x41\x64\x64HoneycombEnvironmentReq\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x18\n\x07\x61pi_key\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\"5\n\x1b\x41\x64\x64HoneycombEnvironmentResp\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\">\n\x1dUpdateHoneycombEnvironmentReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61pi_key\x18\x02 \x01(\t\" \n\x1eUpdateHoneycombEnvironmentResp\"-\n\x1d\x44\x65leteHoneycombEnvironmentReq\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\x1e\x44\x65leteHoneycombEnvironmentResp\"\x17\n\x15UninstallHoneycombReq\"1\n\x16UninstallHoneycombResp\x12\x17\n\x0fintegration_ids\x18\x01 \x03(\t\"\x85\x01\n\x12\x43reateGitHubAppReq\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x03\x12\x13\n\x0bprivate_key\x18\x02 \x01(\t\x12\x15\n\rclient_secret\x18\x03 \x01(\t\x12\x16\n\x0ewebhook_secret\x18\x04 \x01(\t\x12\x1b\n\x13github_organization\x18\x05 \x01(\t\"-\n\x13\x43reateGitHubAppResp\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\"+\n\x10InstallGitHubReq\x12\x17\n\x0finstallation_id\x18\x01 \x01(\x03\"\x13\n\x11InstallGitHubResp\"5\n\x0bIntegration\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"\x15\n\x13ListIntegrationsReq\"L\n\x14ListIntegrationsResp\x12\x34\n\x0cintegrations\x18\x01 \x03(\x0b\x32\x1e.prodvana.workflow.Integration\".\n\x14\x44\x65leteIntegrationReq\x12\x16\n\x0eintegration_id\x18\x01 \x01(\t\"\x17\n\x15\x44\x65leteIntegrationResp\",\n\x16GetInstallGitHubUrlReq\x12\x12\n\ngithub_org\x18\x01 \x01(\t\"8\n\x17GetInstallGitHubUrlResp\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x10\n\x08manifest\x18\x02 \x01(\t*9\n\x0cRegistryType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0f\x44OCKER_REGISTRY\x10\x01\x12\x07\n\x03\x45\x43R\x10\x02*J\n\x0eRegistryStatus\x12\r\n\tUNDEFINED\x10\x00\x12\r\n\tCONNECTED\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x12\x0e\n\nRS_PENDING\x10\x03*E\n\x0bIndexStatus\x12\x0e\n\nIS_UNKNOWN\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0c\n\x08INDEXING\x10\x02\x12\x0b\n\x07INDEXED\x10\x03\x32\xfb*\n\x0fWorkflowManager\x12}\n\x10ListIntegrations\x12&.prodvana.workflow.ListIntegrationsReq\x1a\'.prodvana.workflow.ListIntegrationsResp\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/integrations\x12\x93\x01\n\x11\x44\x65leteIntegration\x12\'.prodvana.workflow.DeleteIntegrationReq\x1a(.prodvana.workflow.DeleteIntegrationResp\"+\x82\xd3\xe4\x93\x02%*#/v1/integrations/{integration_id=*}\x12\xcf\x01\n\"CreateContainerRegistryIntegration\x12\x38.prodvana.workflow.CreateContainerRegistryIntegrationReq\x1a\x38.prodvana.workflow.CreateContainerRegistryIntegrationRes\"5\x82\xd3\xe4\x93\x02/\"*/v1/integrations/container-registry/create:\x01*\x12\xd8\x01\n\"DeleteContainerRegistryIntegration\x12\x38.prodvana.workflow.DeleteContainerRegistryIntegrationReq\x1a\x39.prodvana.workflow.DeleteContainerRegistryIntegrationResp\"=\x82\xd3\xe4\x93\x02\x37*5/v1/integrations/container-registry/{registry_name=*}\x12\xc3\x01\n!ListContainerRegistryIntegrations\x12\x37.prodvana.workflow.ListContainerRegistryIntegrationsReq\x1a\x38.prodvana.workflow.ListContainerRegistryIntegrationsResp\"+\x82\xd3\xe4\x93\x02%\x12#/v1/integrations/container-registry\x12\xcf\x01\n\x1fGetContainerRegistryIntegration\x12\x35.prodvana.workflow.GetContainerRegistryIntegrationReq\x1a\x36.prodvana.workflow.GetContainerRegistryIntegrationResp\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/v1/integrations/container-registry/{registry_name=*}\x12\xb1\x01\n\x13GetServiceImageInfo\x12).prodvana.workflow.GetServiceImageInfoReq\x1a*.prodvana.workflow.GetServiceImageInfoResp\"C\x82\xd3\xe4\x93\x02=\x12;/v1/applications/{application=*}/services/{service=*}/image\x12\xb4\x01\n\x1aGetContainerRegistryImages\x12\x30.prodvana.workflow.GetContainerRegistryImagesReq\x1a\x30.prodvana.workflow.GetContainerRegistryImagesRes\"2\x82\xd3\xe4\x93\x02,\x12*/v1/integrations/{integration_id=*}/images\x12\xba\x01\n\x1cListTrackedImageRepositories\x12\x32.prodvana.workflow.ListTrackedImageRepositoriesReq\x1a\x33.prodvana.workflow.ListTrackedImageRepositoriesResp\"1\x82\xd3\xe4\x93\x02+\x12)/v1/integrations/{integration_id=*}/repos\x12\xbf\x01\n\x19GetTrackedImageRepository\x12/.prodvana.workflow.GetTrackedImageRepositoryReq\x1a\x30.prodvana.workflow.GetTrackedImageRepositoryResp\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/v1/integrations/{integration_id=*}/repo/{repository=*}\x12\xb1\x01\n\x16TrackImageRepositories\x12,.prodvana.workflow.TrackImageRepositoriesReq\x1a-.prodvana.workflow.TrackImageRepositoriesResp\":\x82\xd3\xe4\x93\x02\x34\"//v1/integrations/{integration_id=*}/repos/track:\x01*\x12\xbf\x01\n\x1bStopTrackingImageRepository\x12\x31.prodvana.workflow.StopTrackingImageRepositoryReq\x1a\x32.prodvana.workflow.StopTrackingImageRepositoryResp\"9\x82\xd3\xe4\x93\x02\x33*1/v1/integrations/{integration_id=*}/repos/untrack\x12\xa7\x01\n\x12GetProgramDefaults\x12(.prodvana.workflow.GetProgramDefaultsReq\x1a).prodvana.workflow.GetProgramDefaultsResp\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/v1/integrations/{integration_id=*}/program-defaults\x12\xa8\x01\n\x12GetImageCommitInfo\x12(.prodvana.workflow.GetImageCommitInfoReq\x1a).prodvana.workflow.GetImageCommitInfoResp\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/v1/integrations/{integration_id=*}/image-commit-info\x12\x7f\n\x0cInstallSlack\x12\".prodvana.workflow.InstallSlackReq\x1a#.prodvana.workflow.InstallSlackResp\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/integrations/slack/install\x12\x87\x01\n\x0eUninstallSlack\x12$.prodvana.workflow.UninstallSlackReq\x1a%.prodvana.workflow.UninstallSlackResp\"(\x82\xd3\xe4\x93\x02\"* /v1/integrations/slack/uninstall\x12\x95\x01\n\x12GetInstallSlackUrl\x12(.prodvana.workflow.GetInstallSlackUrlReq\x1a).prodvana.workflow.GetInstallSlackUrlResp\"*\x82\xd3\xe4\x93\x02$\x12\"/v1/integrations/slack/install-url\x12\x8f\x01\n\x10InstallPagerDuty\x12&.prodvana.workflow.InstallPagerDutyReq\x1a\'.prodvana.workflow.InstallPagerDutyResp\"*\x82\xd3\xe4\x93\x02$\x12\"/v1/integrations/pagerduty/install\x12\xa5\x01\n\x16GetInstallPagerDutyUrl\x12,.prodvana.workflow.GetInstallPagerDutyUrlReq\x1a-.prodvana.workflow.GetInstallPagerDutyUrlResp\".\x82\xd3\xe4\x93\x02(\x12&/v1/integrations/pagerduty/install-url\x12\x97\x01\n\x12UninstallPagerDuty\x12(.prodvana.workflow.UninstallPagerDutyReq\x1a).prodvana.workflow.UninstallPagerDutyResp\",\x82\xd3\xe4\x93\x02&*$/v1/integrations/pagerduty/uninstall\x12\x97\x01\n\x16GetGrafanaInstallation\x12,.prodvana.workflow.GetGrafanaInstallationReq\x1a-.prodvana.workflow.GetGrafanaInstallationResp\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/integrations/grafana\x12\x8a\x01\n\x0eInstallGrafana\x12$.prodvana.workflow.InstallGrafanaReq\x1a%.prodvana.workflow.InstallGrafanaResp\"+\x82\xd3\xe4\x93\x02%\" /v1/integrations/grafana/install:\x01*\x12\x8f\x01\n\x10UninstallGrafana\x12&.prodvana.workflow.UninstallGrafanaReq\x1a\'.prodvana.workflow.UninstallGrafanaResp\"*\x82\xd3\xe4\x93\x02$*\"/v1/integrations/grafana/uninstall\x12\xae\x01\n\x19ListHoneycombEnvironments\x12/.prodvana.workflow.ListHoneycombEnvironmentsReq\x1a\x30.prodvana.workflow.ListHoneycombEnvironmentsResp\".\x82\xd3\xe4\x93\x02(\x12&/v1/integrations/honeycomb/environment\x12\xab\x01\n\x17\x41\x64\x64HoneycombEnvironment\x12-.prodvana.workflow.AddHoneycombEnvironmentReq\x1a..prodvana.workflow.AddHoneycombEnvironmentResp\"1\x82\xd3\xe4\x93\x02+\"&/v1/integrations/honeycomb/environment:\x01*\x12\xbd\x01\n\x1aUpdateHoneycombEnvironment\x12\x30.prodvana.workflow.UpdateHoneycombEnvironmentReq\x1a\x31.prodvana.workflow.UpdateHoneycombEnvironmentResp\":\x82\xd3\xe4\x93\x02\x34\x1a//v1/integrations/honeycomb/environment/{name=*}:\x01*\x12\xba\x01\n\x1a\x44\x65leteHoneycombEnvironment\x12\x30.prodvana.workflow.DeleteHoneycombEnvironmentReq\x1a\x31.prodvana.workflow.DeleteHoneycombEnvironmentResp\"7\x82\xd3\xe4\x93\x02\x31*//v1/integrations/honeycomb/environment/{name=*}\x12\x8d\x01\n\x12UninstallHoneycomb\x12(.prodvana.workflow.UninstallHoneycombReq\x1a).prodvana.workflow.UninstallHoneycombResp\"\"\x82\xd3\xe4\x93\x02\x1c*\x1a/v1/integrations/honeycomb\x12\x99\x01\n\x13GetInstallGitHubUrl\x12).prodvana.workflow.GetInstallGitHubUrlReq\x1a*.prodvana.workflow.GetInstallGitHubUrlResp\"+\x82\xd3\xe4\x93\x02%\x12#/v1/integrations/github/install-url\x12\x88\x01\n\x0f\x43reateGitHubApp\x12%.prodvana.workflow.CreateGitHubAppReq\x1a&.prodvana.workflow.CreateGitHubAppResp\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/integrations/github/create\x12\x83\x01\n\rInstallGitHub\x12#.prodvana.workflow.InstallGitHubReq\x1a$.prodvana.workflow.InstallGitHubResp\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/integrations/github/install\x12\x87\x01\n\x0fListRepoCommits\x12%.prodvana.workflow.ListRepoCommitsReq\x1a&.prodvana.workflow.ListRepoCommitsResp\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/integrations/repo/commits\x12\x85\x01\n\rGetCommitInfo\x12#.prodvana.workflow.GetCommitInfoReq\x1a$.prodvana.workflow.GetCommitInfoResp\")\x82\xd3\xe4\x93\x02#\x12!/v1/integrations/repo/commit-infoBMZKgithub.com/prodvana/prodvana-public/go/prodvana-sdk/proto/prodvana/workflowb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'prodvana.workflow.workflow_manager_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZKgithub.com/prodvana/prodvana-public/go/prodvana-sdk/proto/prodvana/workflow'
  _CREATECONTAINERREGISTRYINTEGRATIONREQ.fields_by_name['name']._options = None
  _CREATECONTAINERREGISTRYINTEGRATIONREQ.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^[a-z]([a-z0-9-]*[a-z0-9]){0,1}$'
  _GETCOMMITINFOREQ.fields_by_name['repository']._options = None
  _GETCOMMITINFOREQ.fields_by_name['repository']._serialized_options = b'\372B\004r\002\020\001'
  _GETCOMMITINFOREQ.fields_by_name['commitId']._options = None
  _GETCOMMITINFOREQ.fields_by_name['commitId']._serialized_options = b'\372B\004r\002\020\001'
  _PROGRAMDEFAULTS_ENVENTRY._options = None
  _PROGRAMDEFAULTS_ENVENTRY._serialized_options = b'8\001'
  _INSTALLGRAFANAREQ.fields_by_name['url']._options = None
  _INSTALLGRAFANAREQ.fields_by_name['url']._serialized_options = b'\372B\004r\002\020\001'
  _INSTALLGRAFANAREQ.fields_by_name['api_token']._options = None
  _INSTALLGRAFANAREQ.fields_by_name['api_token']._serialized_options = b'\372B\004r\002\020\001'
  _ADDHONEYCOMBENVIRONMENTREQ.fields_by_name['name']._options = None
  _ADDHONEYCOMBENVIRONMENTREQ.fields_by_name['name']._serialized_options = b'\372B\004r\002\020\001'
  _ADDHONEYCOMBENVIRONMENTREQ.fields_by_name['api_key']._options = None
  _ADDHONEYCOMBENVIRONMENTREQ.fields_by_name['api_key']._serialized_options = b'\372B\004r\002\020\001'
  _WORKFLOWMANAGER.methods_by_name['ListIntegrations']._options = None
  _WORKFLOWMANAGER.methods_by_name['ListIntegrations']._serialized_options = b'\202\323\344\223\002\022\022\020/v1/integrations'
  _WORKFLOWMANAGER.methods_by_name['DeleteIntegration']._options = None
  _WORKFLOWMANAGER.methods_by_name['DeleteIntegration']._serialized_options = b'\202\323\344\223\002%*#/v1/integrations/{integration_id=*}'
  _WORKFLOWMANAGER.methods_by_name['CreateContainerRegistryIntegration']._options = None
  _WORKFLOWMANAGER.methods_by_name['CreateContainerRegistryIntegration']._serialized_options = b'\202\323\344\223\002/\"*/v1/integrations/container-registry/create:\001*'
  _WORKFLOWMANAGER.methods_by_name['DeleteContainerRegistryIntegration']._options = None
  _WORKFLOWMANAGER.methods_by_name['DeleteContainerRegistryIntegration']._serialized_options = b'\202\323\344\223\0027*5/v1/integrations/container-registry/{registry_name=*}'
  _WORKFLOWMANAGER.methods_by_name['ListContainerRegistryIntegrations']._options = None
  _WORKFLOWMANAGER.methods_by_name['ListContainerRegistryIntegrations']._serialized_options = b'\202\323\344\223\002%\022#/v1/integrations/container-registry'
  _WORKFLOWMANAGER.methods_by_name['GetContainerRegistryIntegration']._options = None
  _WORKFLOWMANAGER.methods_by_name['GetContainerRegistryIntegration']._serialized_options = b'\202\323\344\223\0027\0225/v1/integrations/container-registry/{registry_name=*}'
  _WORKFLOWMANAGER.methods_by_name['GetServiceImageInfo']._options = None
  _WORKFLOWMANAGER.methods_by_name['GetServiceImageInfo']._serialized_options = b'\202\323\344\223\002=\022;/v1/applications/{application=*}/services/{service=*}/image'
  _WORKFLOWMANAGER.methods_by_name['GetContainerRegistryImages']._options = None
  _WORKFLOWMANAGER.methods_by_name['GetContainerRegistryImages']._serialized_options = b'\202\323\344\223\002,\022*/v1/integrations/{integration_id=*}/images'
  _WORKFLOWMANAGER.methods_by_name['ListTrackedImageRepositories']._options = None
  _WORKFLOWMANAGER.methods_by_name['ListTrackedImageRepositories']._serialized_options = b'\202\323\344\223\002+\022)/v1/integrations/{integration_id=*}/repos'
  _WORKFLOWMANAGER.methods_by_name['GetTrackedImageRepository']._options = None
  _WORKFLOWMANAGER.methods_by_name['GetTrackedImageRepository']._serialized_options = b'\202\323\344\223\0029\0227/v1/integrations/{integration_id=*}/repo/{repository=*}'
  _WORKFLOWMANAGER.methods_by_name['TrackImageRepositories']._options = None
  _WORKFLOWMANAGER.methods_by_name['TrackImageRepositories']._serialized_options = b'\202\323\344\223\0024\"//v1/integrations/{integration_id=*}/repos/track:\001*'
  _WORKFLOWMANAGER.methods_by_name['StopTrackingImageRepository']._options = None
  _WORKFLOWMANAGER.methods_by_name['StopTrackingImageRepository']._serialized_options = b'\202\323\344\223\0023*1/v1/integrations/{integration_id=*}/repos/untrack'
  _WORKFLOWMANAGER.methods_by_name['GetProgramDefaults']._options = None
  _WORKFLOWMANAGER.methods_by_name['GetProgramDefaults']._serialized_options = b'\202\323\344\223\0026\0224/v1/integrations/{integration_id=*}/program-defaults'
  _WORKFLOWMANAGER.methods_by_name['GetImageCommitInfo']._options = None
  _WORKFLOWMANAGER.methods_by_name['GetImageCommitInfo']._serialized_options = b'\202\323\344\223\0027\0225/v1/integrations/{integration_id=*}/image-commit-info'
  _WORKFLOWMANAGER.methods_by_name['InstallSlack']._options = None
  _WORKFLOWMANAGER.methods_by_name['InstallSlack']._serialized_options = b'\202\323\344\223\002 \022\036/v1/integrations/slack/install'
  _WORKFLOWMANAGER.methods_by_name['UninstallSlack']._options = None
  _WORKFLOWMANAGER.methods_by_name['UninstallSlack']._serialized_options = b'\202\323\344\223\002\"* /v1/integrations/slack/uninstall'
  _WORKFLOWMANAGER.methods_by_name['GetInstallSlackUrl']._options = None
  _WORKFLOWMANAGER.methods_by_name['GetInstallSlackUrl']._serialized_options = b'\202\323\344\223\002$\022\"/v1/integrations/slack/install-url'
  _WORKFLOWMANAGER.methods_by_name['InstallPagerDuty']._options = None
  _WORKFLOWMANAGER.methods_by_name['InstallPagerDuty']._serialized_options = b'\202\323\344\223\002$\022\"/v1/integrations/pagerduty/install'
  _WORKFLOWMANAGER.methods_by_name['GetInstallPagerDutyUrl']._options = None
  _WORKFLOWMANAGER.methods_by_name['GetInstallPagerDutyUrl']._serialized_options = b'\202\323\344\223\002(\022&/v1/integrations/pagerduty/install-url'
  _WORKFLOWMANAGER.methods_by_name['UninstallPagerDuty']._options = None
  _WORKFLOWMANAGER.methods_by_name['UninstallPagerDuty']._serialized_options = b'\202\323\344\223\002&*$/v1/integrations/pagerduty/uninstall'
  _WORKFLOWMANAGER.methods_by_name['GetGrafanaInstallation']._options = None
  _WORKFLOWMANAGER.methods_by_name['GetGrafanaInstallation']._serialized_options = b'\202\323\344\223\002\032\022\030/v1/integrations/grafana'
  _WORKFLOWMANAGER.methods_by_name['InstallGrafana']._options = None
  _WORKFLOWMANAGER.methods_by_name['InstallGrafana']._serialized_options = b'\202\323\344\223\002%\" /v1/integrations/grafana/install:\001*'
  _WORKFLOWMANAGER.methods_by_name['UninstallGrafana']._options = None
  _WORKFLOWMANAGER.methods_by_name['UninstallGrafana']._serialized_options = b'\202\323\344\223\002$*\"/v1/integrations/grafana/uninstall'
  _WORKFLOWMANAGER.methods_by_name['ListHoneycombEnvironments']._options = None
  _WORKFLOWMANAGER.methods_by_name['ListHoneycombEnvironments']._serialized_options = b'\202\323\344\223\002(\022&/v1/integrations/honeycomb/environment'
  _WORKFLOWMANAGER.methods_by_name['AddHoneycombEnvironment']._options = None
  _WORKFLOWMANAGER.methods_by_name['AddHoneycombEnvironment']._serialized_options = b'\202\323\344\223\002+\"&/v1/integrations/honeycomb/environment:\001*'
  _WORKFLOWMANAGER.methods_by_name['UpdateHoneycombEnvironment']._options = None
  _WORKFLOWMANAGER.methods_by_name['UpdateHoneycombEnvironment']._serialized_options = b'\202\323\344\223\0024\032//v1/integrations/honeycomb/environment/{name=*}:\001*'
  _WORKFLOWMANAGER.methods_by_name['DeleteHoneycombEnvironment']._options = None
  _WORKFLOWMANAGER.methods_by_name['DeleteHoneycombEnvironment']._serialized_options = b'\202\323\344\223\0021*//v1/integrations/honeycomb/environment/{name=*}'
  _WORKFLOWMANAGER.methods_by_name['UninstallHoneycomb']._options = None
  _WORKFLOWMANAGER.methods_by_name['UninstallHoneycomb']._serialized_options = b'\202\323\344\223\002\034*\032/v1/integrations/honeycomb'
  _WORKFLOWMANAGER.methods_by_name['GetInstallGitHubUrl']._options = None
  _WORKFLOWMANAGER.methods_by_name['GetInstallGitHubUrl']._serialized_options = b'\202\323\344\223\002%\022#/v1/integrations/github/install-url'
  _WORKFLOWMANAGER.methods_by_name['CreateGitHubApp']._options = None
  _WORKFLOWMANAGER.methods_by_name['CreateGitHubApp']._serialized_options = b'\202\323\344\223\002 \022\036/v1/integrations/github/create'
  _WORKFLOWMANAGER.methods_by_name['InstallGitHub']._options = None
  _WORKFLOWMANAGER.methods_by_name['InstallGitHub']._serialized_options = b'\202\323\344\223\002!\022\037/v1/integrations/github/install'
  _WORKFLOWMANAGER.methods_by_name['ListRepoCommits']._options = None
  _WORKFLOWMANAGER.methods_by_name['ListRepoCommits']._serialized_options = b'\202\323\344\223\002\037\022\035/v1/integrations/repo/commits'
  _WORKFLOWMANAGER.methods_by_name['GetCommitInfo']._options = None
  _WORKFLOWMANAGER.methods_by_name['GetCommitInfo']._serialized_options = b'\202\323\344\223\002#\022!/v1/integrations/repo/commit-info'
  _globals['_REGISTRYTYPE']._serialized_start=6828
  _globals['_REGISTRYTYPE']._serialized_end=6885
  _globals['_REGISTRYSTATUS']._serialized_start=6887
  _globals['_REGISTRYSTATUS']._serialized_end=6961
  _globals['_INDEXSTATUS']._serialized_start=6963
  _globals['_INDEXSTATUS']._serialized_end=7032
  _globals['_TRACKEDIMAGEREPOSITORY']._serialized_start=250
  _globals['_TRACKEDIMAGEREPOSITORY']._serialized_end=396
  _globals['_REGISTRYIMAGE']._serialized_start=399
  _globals['_REGISTRYIMAGE']._serialized_end=550
  _globals['_LISTREPOCOMMITSREQ']._serialized_start=552
  _globals['_LISTREPOCOMMITSREQ']._serialized_end=653
  _globals['_LISTREPOCOMMITSRESP']._serialized_start=655
  _globals['_LISTREPOCOMMITSRESP']._serialized_end=741
  _globals['_CREATECONTAINERREGISTRYINTEGRATIONREQ']._serialized_start=744
  _globals['_CREATECONTAINERREGISTRYINTEGRATIONREQ']._serialized_end=1276
  _globals['_CREATECONTAINERREGISTRYINTEGRATIONREQ_ECROPTIONS']._serialized_start=1145
  _globals['_CREATECONTAINERREGISTRYINTEGRATIONREQ_ECROPTIONS']._serialized_end=1231
  _globals['_CREATECONTAINERREGISTRYINTEGRATIONREQ_PUBLICREGISTRYOPTIONS']._serialized_start=1233
  _globals['_CREATECONTAINERREGISTRYINTEGRATIONREQ_PUBLICREGISTRYOPTIONS']._serialized_end=1256
  _globals['_CREATECONTAINERREGISTRYINTEGRATIONRES']._serialized_start=1278
  _globals['_CREATECONTAINERREGISTRYINTEGRATIONRES']._serialized_end=1341
  _globals['_DELETECONTAINERREGISTRYINTEGRATIONREQ']._serialized_start=1343
  _globals['_DELETECONTAINERREGISTRYINTEGRATIONREQ']._serialized_end=1405
  _globals['_DELETECONTAINERREGISTRYINTEGRATIONRESP']._serialized_start=1407
  _globals['_DELETECONTAINERREGISTRYINTEGRATIONRESP']._serialized_end=1447
  _globals['_LISTCONTAINERREGISTRYINTEGRATIONSREQ']._serialized_start=1449
  _globals['_LISTCONTAINERREGISTRYINTEGRATIONSREQ']._serialized_end=1509
  _globals['_CONTAINERREGISTRYINTEGRATION']._serialized_start=1512
  _globals['_CONTAINERREGISTRYINTEGRATION']._serialized_end=1844
  _globals['_CONTAINERREGISTRYINTEGRATION_ECRINFO']._serialized_start=1802
  _globals['_CONTAINERREGISTRYINTEGRATION_ECRINFO']._serialized_end=1827
  _globals['_LISTCONTAINERREGISTRYINTEGRATIONSRESP']._serialized_start=1847
  _globals['_LISTCONTAINERREGISTRYINTEGRATIONSRESP']._serialized_end=2327
  _globals['_LISTCONTAINERREGISTRYINTEGRATIONSRESP_ECRINFO']._serialized_start=1802
  _globals['_LISTCONTAINERREGISTRYINTEGRATIONSRESP_ECRINFO']._serialized_end=1827
  _globals['_LISTCONTAINERREGISTRYINTEGRATIONSRESP_CONTAINERREGISTRYINTEGRATIONINFO']._serialized_start=2037
  _globals['_LISTCONTAINERREGISTRYINTEGRATIONSRESP_CONTAINERREGISTRYINTEGRATIONINFO']._serialized_end=2327
  _globals['_GETCONTAINERREGISTRYINTEGRATIONREQ']._serialized_start=2329
  _globals['_GETCONTAINERREGISTRYINTEGRATIONREQ']._serialized_end=2388
  _globals['_GETCONTAINERREGISTRYINTEGRATIONRESP']._serialized_start=2390
  _globals['_GETCONTAINERREGISTRYINTEGRATIONRESP']._serialized_end=2494
  _globals['_GETCONTAINERREGISTRYIMAGESREQ']._serialized_start=2497
  _globals['_GETCONTAINERREGISTRYIMAGESREQ']._serialized_end=2646
  _globals['_GETCONTAINERREGISTRYIMAGESRES']._serialized_start=2648
  _globals['_GETCONTAINERREGISTRYIMAGESRES']._serialized_end=2754
  _globals['_LISTTRACKEDIMAGEREPOSITORIESREQ']._serialized_start=2756
  _globals['_LISTTRACKEDIMAGEREPOSITORIESREQ']._serialized_end=2813
  _globals['_LISTTRACKEDIMAGEREPOSITORIESRESP']._serialized_start=2815
  _globals['_LISTTRACKEDIMAGEREPOSITORIESRESP']._serialized_end=2914
  _globals['_GETTRACKEDIMAGEREPOSITORYREQ']._serialized_start=2916
  _globals['_GETTRACKEDIMAGEREPOSITORYREQ']._serialized_end=2990
  _globals['_GETTRACKEDIMAGEREPOSITORYRESP']._serialized_start=2992
  _globals['_GETTRACKEDIMAGEREPOSITORYRESP']._serialized_end=3086
  _globals['_TRACKIMAGEREPOSITORIESREQ']._serialized_start=3088
  _globals['_TRACKIMAGEREPOSITORIESREQ']._serialized_end=3161
  _globals['_TRACKIMAGEREPOSITORIESRESP']._serialized_start=3163
  _globals['_TRACKIMAGEREPOSITORIESRESP']._serialized_end=3191
  _globals['_STOPTRACKINGIMAGEREPOSITORYREQ']._serialized_start=3193
  _globals['_STOPTRACKINGIMAGEREPOSITORYREQ']._serialized_end=3269
  _globals['_STOPTRACKINGIMAGEREPOSITORYRESP']._serialized_start=3271
  _globals['_STOPTRACKINGIMAGEREPOSITORYRESP']._serialized_end=3304
  _globals['_GETIMAGECOMMITINFOREQ']._serialized_start=3306
  _globals['_GETIMAGECOMMITINFOREQ']._serialized_end=3423
  _globals['_GETIMAGECOMMITINFORESP']._serialized_start=3425
  _globals['_GETIMAGECOMMITINFORESP']._serialized_end=3508
  _globals['_GETCOMMITINFOREQ']._serialized_start=3510
  _globals['_GETCOMMITINFOREQ']._serialized_end=3584
  _globals['_GETCOMMITINFORESP']._serialized_start=3586
  _globals['_GETCOMMITINFORESP']._serialized_end=3644
  _globals['_GETPROGRAMDEFAULTSREQ']._serialized_start=3647
  _globals['_GETPROGRAMDEFAULTSREQ']._serialized_end=3793
  _globals['_PROGRAMDEFAULTS']._serialized_start=3796
  _globals['_PROGRAMDEFAULTS']._serialized_end=4033
  _globals['_PROGRAMDEFAULTS_ENVENTRY']._serialized_start=3957
  _globals['_PROGRAMDEFAULTS_ENVENTRY']._serialized_end=4033
  _globals['_GETPROGRAMDEFAULTSRESP']._serialized_start=4035
  _globals['_GETPROGRAMDEFAULTSRESP']._serialized_end=4121
  _globals['_GETSERVICEIMAGEINFOREQ']._serialized_start=4123
  _globals['_GETSERVICEIMAGEINFOREQ']._serialized_end=4203
  _globals['_GETSERVICEIMAGEINFORESP']._serialized_start=4206
  _globals['_GETSERVICEIMAGEINFORESP']._serialized_end=4742
  _globals['_GETSERVICEIMAGEINFORESP_VERSIONINFO']._serialized_start=4355
  _globals['_GETSERVICEIMAGEINFORESP_VERSIONINFO']._serialized_end=4555
  _globals['_GETSERVICEIMAGEINFORESP_PROGRAMINFO']._serialized_start=4557
  _globals['_GETSERVICEIMAGEINFORESP_PROGRAMINFO']._serialized_end=4617
  _globals['_GETSERVICEIMAGEINFORESP_PERRELEASECHANNEL']._serialized_start=4619
  _globals['_GETSERVICEIMAGEINFORESP_PERRELEASECHANNEL']._serialized_end=4742
  _globals['_INSTALLSLACKREQ']._serialized_start=4744
  _globals['_INSTALLSLACKREQ']._serialized_end=4812
  _globals['_INSTALLSLACKRESP']._serialized_start=4814
  _globals['_INSTALLSLACKRESP']._serialized_end=4866
  _globals['_GETINSTALLSLACKURLREQ']._serialized_start=4868
  _globals['_GETINSTALLSLACKURLREQ']._serialized_end=4891
  _globals['_GETINSTALLSLACKURLRESP']._serialized_start=4893
  _globals['_GETINSTALLSLACKURLRESP']._serialized_end=4930
  _globals['_UNINSTALLSLACKREQ']._serialized_start=4932
  _globals['_UNINSTALLSLACKREQ']._serialized_end=4951
  _globals['_UNINSTALLSLACKRESP']._serialized_start=4953
  _globals['_UNINSTALLSLACKRESP']._serialized_end=4990
  _globals['_SLACKCHANNEL']._serialized_start=4992
  _globals['_SLACKCHANNEL']._serialized_end=5032
  _globals['_INSTALLPAGERDUTYREQ']._serialized_start=5034
  _globals['_INSTALLPAGERDUTYREQ']._serialized_end=5106
  _globals['_INSTALLPAGERDUTYRESP']._serialized_start=5108
  _globals['_INSTALLPAGERDUTYRESP']._serialized_end=5164
  _globals['_GETINSTALLPAGERDUTYURLREQ']._serialized_start=5166
  _globals['_GETINSTALLPAGERDUTYURLREQ']._serialized_end=5193
  _globals['_GETINSTALLPAGERDUTYURLRESP']._serialized_start=5195
  _globals['_GETINSTALLPAGERDUTYURLRESP']._serialized_end=5236
  _globals['_UNINSTALLPAGERDUTYREQ']._serialized_start=5238
  _globals['_UNINSTALLPAGERDUTYREQ']._serialized_end=5261
  _globals['_UNINSTALLPAGERDUTYRESP']._serialized_start=5263
  _globals['_UNINSTALLPAGERDUTYRESP']._serialized_end=5304
  _globals['_PAGERDUTYSERVICE']._serialized_start=5306
  _globals['_PAGERDUTYSERVICE']._serialized_end=5350
  _globals['_INSTALLGRAFANAREQ']._serialized_start=5352
  _globals['_INSTALLGRAFANAREQ']._serialized_end=5421
  _globals['_INSTALLGRAFANARESP']._serialized_start=5423
  _globals['_INSTALLGRAFANARESP']._serialized_end=5467
  _globals['_UNINSTALLGRAFANAREQ']._serialized_start=5469
  _globals['_UNINSTALLGRAFANAREQ']._serialized_end=5490
  _globals['_UNINSTALLGRAFANARESP']._serialized_start=5492
  _globals['_UNINSTALLGRAFANARESP']._serialized_end=5538
  _globals['_GETGRAFANAINSTALLATIONREQ']._serialized_start=5540
  _globals['_GETGRAFANAINSTALLATIONREQ']._serialized_end=5567
  _globals['_GETGRAFANAINSTALLATIONRESP']._serialized_start=5569
  _globals['_GETGRAFANAINSTALLATIONRESP']._serialized_end=5634
  _globals['_LISTHONEYCOMBENVIRONMENTSREQ']._serialized_start=5636
  _globals['_LISTHONEYCOMBENVIRONMENTSREQ']._serialized_end=5666
  _globals['_LISTHONEYCOMBENVIRONMENTSRESP']._serialized_start=5669
  _globals['_LISTHONEYCOMBENVIRONMENTSRESP']._serialized_end=5855
  _globals['_LISTHONEYCOMBENVIRONMENTSRESP_HONEYCOMBENVIRONMENT']._serialized_start=5795
  _globals['_LISTHONEYCOMBENVIRONMENTSRESP_HONEYCOMBENVIRONMENT']._serialized_end=5855
  _globals['_ADDHONEYCOMBENVIRONMENTREQ']._serialized_start=5857
  _globals['_ADDHONEYCOMBENVIRONMENTREQ']._serialized_end=5934
  _globals['_ADDHONEYCOMBENVIRONMENTRESP']._serialized_start=5936
  _globals['_ADDHONEYCOMBENVIRONMENTRESP']._serialized_end=5989
  _globals['_UPDATEHONEYCOMBENVIRONMENTREQ']._serialized_start=5991
  _globals['_UPDATEHONEYCOMBENVIRONMENTREQ']._serialized_end=6053
  _globals['_UPDATEHONEYCOMBENVIRONMENTRESP']._serialized_start=6055
  _globals['_UPDATEHONEYCOMBENVIRONMENTRESP']._serialized_end=6087
  _globals['_DELETEHONEYCOMBENVIRONMENTREQ']._serialized_start=6089
  _globals['_DELETEHONEYCOMBENVIRONMENTREQ']._serialized_end=6134
  _globals['_DELETEHONEYCOMBENVIRONMENTRESP']._serialized_start=6136
  _globals['_DELETEHONEYCOMBENVIRONMENTRESP']._serialized_end=6168
  _globals['_UNINSTALLHONEYCOMBREQ']._serialized_start=6170
  _globals['_UNINSTALLHONEYCOMBREQ']._serialized_end=6193
  _globals['_UNINSTALLHONEYCOMBRESP']._serialized_start=6195
  _globals['_UNINSTALLHONEYCOMBRESP']._serialized_end=6244
  _globals['_CREATEGITHUBAPPREQ']._serialized_start=6247
  _globals['_CREATEGITHUBAPPREQ']._serialized_end=6380
  _globals['_CREATEGITHUBAPPRESP']._serialized_start=6382
  _globals['_CREATEGITHUBAPPRESP']._serialized_end=6427
  _globals['_INSTALLGITHUBREQ']._serialized_start=6429
  _globals['_INSTALLGITHUBREQ']._serialized_end=6472
  _globals['_INSTALLGITHUBRESP']._serialized_start=6474
  _globals['_INSTALLGITHUBRESP']._serialized_end=6493
  _globals['_INTEGRATION']._serialized_start=6495
  _globals['_INTEGRATION']._serialized_end=6548
  _globals['_LISTINTEGRATIONSREQ']._serialized_start=6550
  _globals['_LISTINTEGRATIONSREQ']._serialized_end=6571
  _globals['_LISTINTEGRATIONSRESP']._serialized_start=6573
  _globals['_LISTINTEGRATIONSRESP']._serialized_end=6649
  _globals['_DELETEINTEGRATIONREQ']._serialized_start=6651
  _globals['_DELETEINTEGRATIONREQ']._serialized_end=6697
  _globals['_DELETEINTEGRATIONRESP']._serialized_start=6699
  _globals['_DELETEINTEGRATIONRESP']._serialized_end=6722
  _globals['_GETINSTALLGITHUBURLREQ']._serialized_start=6724
  _globals['_GETINSTALLGITHUBURLREQ']._serialized_end=6768
  _globals['_GETINSTALLGITHUBURLRESP']._serialized_start=6770
  _globals['_GETINSTALLGITHUBURLRESP']._serialized_end=6826
  _globals['_WORKFLOWMANAGER']._serialized_start=7035
  _globals['_WORKFLOWMANAGER']._serialized_end=12534
# @@protoc_insertion_point(module_scope)
