#!/usr/bin/env python3

def flatten_structure(structure, parent_path=None, depth=0):
    """Aplatit une structure hiérarchique de groupes et projets."""
    groups = []
    projects = []
    
    for group in structure:

        group_path = group.get('path', group['name'].lower().replace(' ', '-'))
        current_full_path = f"{parent_path}/{group_path}" if parent_path else group_path
        

        group_data = {
            'name': group['name'],
            'description': group.get('description', ''),
            'visibility': group.get('visibility', 'private'),
            'path': group_path,
            'depth': depth,
        }
        
        if parent_path:
            group_data['parent'] = parent_path 
            
        groups.append(group_data)
        
        if 'projects' in group and group['projects']:
            for project in group['projects']:
                project_data = project.copy()
                project_data['group'] = group['name']
                project_data['group_path'] = current_full_path
                projects.append(project_data)
        
        if 'subgroups' in group and group['subgroups']:
            sub_results = flatten_structure(group['subgroups'], current_full_path, depth + 1)
            groups.extend(sub_results['groups'])
            projects.extend(sub_results['projects'])
    
    return {'groups': groups, 'projects': projects}



class FilterModule(object):
    def filters(self):
        return {
            'flatten_structure': flatten_structure
        }
