{{- define "devops-chart.fullname" -}}
{{- printf "%s" .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{- define "devops-chart.labels" -}}
app.kubernetes.io/name: {{ include "devops-chart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.Version }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{- define "devops-chart.name" -}}
{{- .Chart.Name -}}
{{- end }}
