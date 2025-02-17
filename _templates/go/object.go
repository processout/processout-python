package processout

import (
	"bytes"
	"encoding/json"
	"net/http"
	"net/url"
	"strings"
	"time"
	"io"

	"gopkg.in/processout.v5/errors"
)

// {{ .V.Name }} represents the {{ .V.Name }} API object 
type {{ .V.Name }} struct {
	{{- range $k, $v := .V.Properties }}
	// {{ capitalize (buildFormatVariable $v.Name) }} is the {{ firstLetterLowercase $v.Description }}
	{{ capitalize (buildFormatVariable $v.Name) }} {{ buildVariableType $v true }} `json:"{{ $v.Name }},omitempty"`
	{{- end }}

	client *ProcessOut
}

{{- range $k, $v := .V.Properties }}
{{ if eq $v.Name "id" }}
// GetID implements the  Identiable interface
func (s *{{ $.V.Name }}) GetID() string {
	if s.ID == nil {
		return ""
	}

	return *s.ID
}
{{- end }}
{{- end }}

// SetClient sets the client for the {{ $.V.Name }} object and its
// children
func (s *{{ $.V.Name }}) SetClient(c *ProcessOut) *{{ $.V.Name }} {
	if s == nil {
		return s
	}
	s.client = c
	{{- range $k, $v := .V.Properties }}
		{{- if and (eq $v.Type "object") (ne $v.Reference "") }}
		if s.{{ capitalize (buildFormatVariable $v.Name) }} != nil {
			s.{{ capitalize (buildFormatVariable $v.Name) }}.SetClient(c)
		}
		{{- end }}
	{{- end }}

	return s
}

// Prefil prefills the object with data provided in the parameter
func (s *{{ $.V.Name }}) Prefill(c *{{ $.V.Name }}) *{{ $.V.Name }} {
	if c == nil {
		return s
	}

	{{ range $i, $v := .V.Properties -}}
	s.{{ capitalize (buildFormatVariable $v.Name) }} = c.{{ capitalize (buildFormatVariable $v.Name) }}
	{{ end }}
	return s
}

{{ range $k, $v := .V.Routes }}
// {{ $.V.Name }}{{ pascalCase $v.Name }}Parameters is the structure representing the 
// additional parameters used to call {{ $.V.Name }}.{{ pascalCase $v.Name }}
type {{ $.V.Name }}{{ pascalCase $v.Name }}Parameters struct {
*Options
*{{ $.V.Name }}
{{ buildParametersOptionsArray $v.AdditionalRequires }}
}
// {{ pascalCase $v.Name }} allows you to {{ firstLetterLowercase $v.Description }}
func (s {{ $.V.Name }}) {{ pascalCase $v.Name }}({{ paramList $.V.Name $v }}options ...{{ $.V.Name }}{{ pascalCase $v.Name }}Parameters) ({{ buildReturnType $v }}) {
	if s.client == nil {
		panic("Please use the client.New{{ $.V.Name }}() method to create a new {{ $.V.Name }} object")
	}
	if len(options) > 1 {
		panic("The options parameter should only be provided once.")
	}

	opt := {{ $.V.Name }}{{ pascalCase $v.Name }}Parameters{}
	if len(options) == 1 {
		opt = options[0]
	}
	if opt.Options == nil {
		opt.Options = &Options{}
	}
	s.Prefill(opt.{{ $.V.Name }})

	type Response struct {
		{{- range $tk, $tv := $v.Produces }}
			{{- if eq $tv.Type "self" }}
				{{ $.V.Name }} *{{ $.V.Name }} `json:"{{ $tv.FieldName }}"`
			{{- else if eq $tv.Type "object" }}
				{{ buildRemovePointer (buildVariableType $tv false) }} {{ buildVariableType $tv false }} `json:"{{ $tv.FieldName }}"`
			{{- else if eq $tv.Type "list" }}
				{{ pascalCase $tv.FieldName }} {{ buildVariableType $tv false }} `json:"{{ $tv.FieldName }}"`
			{{ end -}}
		{{ end }}
		HasMore bool `json:"has_more"`
		Success bool `json:"success"`
		Message string `json:"message"`
		Code    string `json:"error_type"`
	}

	data := struct{
		*Options
{{ buildParametersArrayStruct $v.Requires $v.AdditionalRequires $v.Parameters -}}		
	}{
		Options: opt.Options,
{{ buildParametersArray $v.Requires $v.AdditionalRequires $v.Parameters -}}
	}

	body, err := json.Marshal(data)
	if err != nil {
		return {{ range $tk, $tv := $v.Produces -}}
			{{- if nequals $tv.Type "boolean" -}}
				nil,
			{{- end -}}
		{{- end -}} errors.New(err, "", "")
	}

	path := "{{ buildPathFromParameters $v.Path $v.Parameters (uncapitalize (camelCase $.V.Name)) }}"

	req, err := http.NewRequest(
		"{{ tu $v.Method }}",
		Host+path,
		bytes.NewReader(body),
	)
	if err != nil {
		return {{ range $tk, $tv := $v.Produces -}}
			{{- if nequals $tv.Type "boolean" -}}
				nil,
			{{- end -}}
		{{- end -}} errors.NewNetworkError(err)
	}
	setupRequest(s.client, opt.Options, req)

	res, err := s.client.HTTPClient.Do(req)
	if err != nil {
		return {{ range $tk, $tv := $v.Produces -}}
			{{- if nequals $tv.Type "boolean" -}}
				nil,
			{{- end -}}
		{{- end -}} errors.NewNetworkError(err)
	}
	payload := &Response{}
	defer res.Body.Close()
	if res.StatusCode >= 500 {
		return {{ range $tk, $tv := $v.Produces -}}
			{{- if nequals $tv.Type "boolean" -}}
				nil,
			{{- end -}}
		{{- end -}} errors.New(nil, "", "An unexpected error occurred while processing your request.. A lot of sweat is already flowing from our developers head!")
	}
	err = json.NewDecoder(res.Body).Decode(payload)
	if err != nil {
		return {{ range $tk, $tv := $v.Produces -}}
			{{- if nequals $tv.Type "boolean" -}}
				nil,
			{{- end -}}
		{{- end -}} errors.New(err, "", "")
	}

	if !payload.Success {
		erri := errors.NewFromResponse(res.StatusCode, payload.Code,
			payload.Message)
		
		return {{ range $tk, $tv := $v.Produces -}}
			{{- if nequals $tv.Type "boolean" -}}
				nil,
			{{- end -}}
		{{- end -}} erri
	}

	{{ range $tk, $tv := $v.Produces -}}
		{{- if eq $tv.Type "self" }}
			payload.{{ $.V.Name }}.SetClient(s.client)
		{{- else if eq $tv.Type "object" }}
			payload.{{ buildRemovePointer (buildVariableType $tv false) }}.SetClient(s.client)
		{{- else if eq $tv.Type "list" }}
			{{ buildFormatVariable $tv.FieldName }}List := []Identifiable{}
			for _, o := range payload.{{ pascalCase $tv.FieldName }} {
				{{ buildFormatVariable $tv.FieldName }}List = append({{ buildFormatVariable $tv.FieldName }}List, o.SetClient(s.client))
			}
			{{ buildFormatVariable $tv.FieldName }}Iterator := &Iterator{
				pos: -1,
				path: path,
				data: {{ buildFormatVariable $tv.FieldName }}List,
				options: opt.Options,
				decoder: func(b io.Reader, i interface{}) (bool, error) {
					r := struct {
						Data json.RawMessage `json:"{{ $tv.FieldName }}"`
						HasMore bool `json:"has_more"`
					}{}
					if err := json.NewDecoder(b).Decode(&r); err != nil {
						return false, err
					}
					if err := json.Unmarshal(r.Data, i); err != nil {
						return false, err
					}
					return r.HasMore, nil
				},
				client: s.client,
				hasMoreNext: payload.HasMore,
				hasMorePrev: false,
			}
		{{- end }}
	{{- end }}
	return {{ range $tk, $tv := $v.Produces -}}
		{{- if nequals $tv.Type "boolean" -}}
			{{- if eq $tv.Type "self" -}}
				payload.{{ $.V.Name }},
			{{- else if eq $tv.Type "object" -}}
				payload.{{ buildRemovePointer (buildVariableType $tv false) }},
			{{- else if eq $tv.Type "list" -}}
				{{ buildFormatVariable $tv.FieldName }}Iterator,
			{{- end -}}
		{{- end -}}
	{{- end -}} nil
}
{{ end }}

// dummy{{ capitalize .V.Name }} is a dummy function that's only
// here because some files need specific packages and some don't.
// It's easier to include it for every file. In case you couldn't
// tell, everything is generated.
func dummy{{ capitalize .V.Name }}() {
	type dummy struct {
		a bytes.Buffer
		b json.RawMessage
		c http.File
		d strings.Reader
		e time.Time
		f url.URL
		g io.Reader
	}
	errors.New(nil, "", "")
}
