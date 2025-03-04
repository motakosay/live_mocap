setup_script = """from setuptools import setup, Extension
import os

module = Extension('cpp_eval_bone_matrix',
                   sources=['cpp_eval_bone_matrix.cpp'])

setup(name='cpp_eval_bone_matrix',
      version='1.0',
      description='Evaluation of Bone Matrix',
      ext_modules=[module])"""

# Write the setup script to a file
with open('/content/live_mocap/cpp_eval_bone_matrix/setup.py', 'w') as f:
    f.write(setup_script)
