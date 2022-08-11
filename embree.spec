#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : embree
Version  : 3.12.0
Release  : 20
URL      : https://github.com/embree/embree/archive/v3.12.0/embree-3.12.0.tar.gz
Source0  : https://github.com/embree/embree/archive/v3.12.0/embree-3.12.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: embree-lib = %{version}-%{release}
Requires: embree-libexec = %{version}-%{release}
Requires: embree-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : embree-dev
BuildRequires : git
BuildRequires : glfw-dev
BuildRequires : glibc-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : llvm
BuildRequires : llvm-dev
BuildRequires : mesa-dev
BuildRequires : oiio-dev
BuildRequires : tbb-dev

%description
% Embree: High Performance Ray Tracing Kernels 3.12.0
% Intel Corporation
Embree Overview
===============

%package dev
Summary: dev components for the embree package.
Group: Development
Requires: embree-lib = %{version}-%{release}
Requires: embree-extras = %{version}-%{release}
Provides: embree-devel = %{version}-%{release}
Requires: embree = %{version}-%{release}

%description dev
dev components for the embree package.


%package doc
Summary: doc components for the embree package.
Group: Documentation

%description doc
doc components for the embree package.


%package extras
Summary: extras components for the embree package.
Group: Default

%description extras
extras components for the embree package.


%package lib
Summary: lib components for the embree package.
Group: Libraries
Requires: embree-libexec = %{version}-%{release}
Requires: embree-license = %{version}-%{release}

%description lib
lib components for the embree package.


%package libexec
Summary: libexec components for the embree package.
Group: Default
Requires: embree-license = %{version}-%{release}

%description libexec
libexec components for the embree package.


%package license
Summary: license components for the embree package.
Group: Default

%description license
license components for the embree package.


%prep
%setup -q -n embree-3.12.0
cd %{_builddir}/embree-3.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618878909
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CFLAGS=${CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CXXFLAGS=${CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
unset LDFLAGS
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DEMBREE_ISPC_SUPPORT=false \
-DTASKING_TBB=true \
-DCMAKE_INSTALL_BINDIR=libexec
make  %{?_smp_mflags}  VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CFLAGS=${CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CXXFLAGS=${CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
unset LDFLAGS
export CFLAGS="$CFLAGS -O3 -fno-lto -march=haswell "
export FCFLAGS="$FFLAGS -O3 -fno-lto -march=haswell "
export FFLAGS="$FFLAGS -O3 -fno-lto -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -fno-lto -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
export FFLAGS="$FFLAGS -march=haswell -m64"
export FCFLAGS="$FCFLAGS -march=haswell -m64"
%cmake .. -DEMBREE_ISPC_SUPPORT=false \
-DTASKING_TBB=true \
-DCMAKE_INSTALL_BINDIR=libexec
make  %{?_smp_mflags}  VERBOSE=1
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CFLAGS=${CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CXXFLAGS=${CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
unset LDFLAGS
export CFLAGS="$CFLAGS -O3 -fno-lto -march=skylake-avx512 "
export FCFLAGS="$FFLAGS -O3 -fno-lto -march=skylake-avx512 "
export FFLAGS="$FFLAGS -O3 -fno-lto -march=skylake-avx512 "
export CXXFLAGS="$CXXFLAGS -O3 -fno-lto -march=skylake-avx512 "
export CFLAGS="$CFLAGS -march=skylake-avx512 -m64 "
export CXXFLAGS="$CXXFLAGS -march=skylake-avx512 -m64 "
export FFLAGS="$FFLAGS -march=skylake-avx512 -m64 "
export FCFLAGS="$FCFLAGS -march=skylake-avx512 -m64 "
%cmake .. -DEMBREE_ISPC_SUPPORT=false \
-DTASKING_TBB=true \
-DCMAKE_INSTALL_BINDIR=libexec
make  %{?_smp_mflags}  VERBOSE=1
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd clr-build; ctest %{?_smp_mflags} -E verify; popd

%install
export SOURCE_DATE_EPOCH=1618878909
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/embree
cp %{_builddir}/embree-3.12.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/embree/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/embree-3.12.0/tutorials/common/glfw/COPYING.txt %{buildroot}/usr/share/package-licenses/embree/d3c41d58a2a6a19465e61e6710203244faec7db2
cp %{_builddir}/embree-3.12.0/tutorials/common/imgui/LICENSE.txt %{buildroot}/usr/share/package-licenses/embree/35c378e9a2394a10656c4f7075323670e5bfd5f5
pushd clr-build-avx512
%make_install_avx512  || :
popd
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/embree3/rtcore.h
/usr/include/embree3/rtcore.isph
/usr/include/embree3/rtcore_buffer.h
/usr/include/embree3/rtcore_buffer.isph
/usr/include/embree3/rtcore_builder.h
/usr/include/embree3/rtcore_common.h
/usr/include/embree3/rtcore_common.isph
/usr/include/embree3/rtcore_config.h
/usr/include/embree3/rtcore_device.h
/usr/include/embree3/rtcore_device.isph
/usr/include/embree3/rtcore_geometry.h
/usr/include/embree3/rtcore_geometry.isph
/usr/include/embree3/rtcore_quaternion.h
/usr/include/embree3/rtcore_quaternion.isph
/usr/include/embree3/rtcore_ray.h
/usr/include/embree3/rtcore_ray.isph
/usr/include/embree3/rtcore_scene.h
/usr/include/embree3/rtcore_scene.isph
/usr/lib64/cmake/embree-3.12.0/embree-config-version.cmake
/usr/lib64/cmake/embree-3.12.0/embree-config.cmake
/usr/lib64/cmake/embree-3.12.0/embree-targets-relwithdebinfo.cmake
/usr/lib64/cmake/embree-3.12.0/embree-targets.cmake
/usr/lib64/haswell/avx512_1/libembree3.so
/usr/lib64/haswell/libembree3.so
/usr/lib64/libembree3.so
/usr/share/man/man3/RTCBufferType.3embree3
/usr/share/man/man3/RTCCurveFlags.3embree3
/usr/share/man/man3/RTCFormat.3embree3
/usr/share/man/man3/RTCHit.3embree3
/usr/share/man/man3/RTCHitN.3embree3
/usr/share/man/man3/RTCQuaternionDecomposition.3embree3
/usr/share/man/man3/RTCRay.3embree3
/usr/share/man/man3/RTCRayHit.3embree3
/usr/share/man/man3/RTCRayHitN.3embree3
/usr/share/man/man3/RTCRayN.3embree3
/usr/share/man/man3/RTC_GEOMETRY_TYPE_CURVE.3embree3
/usr/share/man/man3/RTC_GEOMETRY_TYPE_GRID.3embree3
/usr/share/man/man3/RTC_GEOMETRY_TYPE_INSTANCE.3embree3
/usr/share/man/man3/RTC_GEOMETRY_TYPE_POINT.3embree3
/usr/share/man/man3/RTC_GEOMETRY_TYPE_QUAD.3embree3
/usr/share/man/man3/RTC_GEOMETRY_TYPE_SUBDIVISION.3embree3
/usr/share/man/man3/RTC_GEOMETRY_TYPE_TRIANGLE.3embree3
/usr/share/man/man3/RTC_GEOMETRY_TYPE_USER.3embree3
/usr/share/man/man3/rtcAttachGeometry.3embree3
/usr/share/man/man3/rtcAttachGeometryByID.3embree3
/usr/share/man/man3/rtcBuildBVH.3embree3
/usr/share/man/man3/rtcCollide.3embree3
/usr/share/man/man3/rtcCommitGeometry.3embree3
/usr/share/man/man3/rtcCommitScene.3embree3
/usr/share/man/man3/rtcDetachGeometry.3embree3
/usr/share/man/man3/rtcDisableGeometry.3embree3
/usr/share/man/man3/rtcEnableGeometry.3embree3
/usr/share/man/man3/rtcFilterIntersection.3embree3
/usr/share/man/man3/rtcFilterOcclusion.3embree3
/usr/share/man/man3/rtcGetBufferData.3embree3
/usr/share/man/man3/rtcGetDeviceError.3embree3
/usr/share/man/man3/rtcGetDeviceProperty.3embree3
/usr/share/man/man3/rtcGetGeometry.3embree3
/usr/share/man/man3/rtcGetGeometryBufferData.3embree3
/usr/share/man/man3/rtcGetGeometryFace.3embree3
/usr/share/man/man3/rtcGetGeometryFirstHalfEdge.3embree3
/usr/share/man/man3/rtcGetGeometryNextHalfEdge.3embree3
/usr/share/man/man3/rtcGetGeometryOppositeHalfEdge.3embree3
/usr/share/man/man3/rtcGetGeometryPreviousHalfEdge.3embree3
/usr/share/man/man3/rtcGetGeometryTransform.3embree3
/usr/share/man/man3/rtcGetGeometryUserData.3embree3
/usr/share/man/man3/rtcGetSceneBounds.3embree3
/usr/share/man/man3/rtcGetSceneDevice.3embree3
/usr/share/man/man3/rtcGetSceneFlags.3embree3
/usr/share/man/man3/rtcGetSceneLinearBounds.3embree3
/usr/share/man/man3/rtcInitIntersectContext.3embree3
/usr/share/man/man3/rtcInitPointQueryContext.3embree3
/usr/share/man/man3/rtcInitPointQueryInstanceStack.3embree3
/usr/share/man/man3/rtcInitQuaternionDecomposition.3embree3
/usr/share/man/man3/rtcInterpolate.3embree3
/usr/share/man/man3/rtcInterpolateN.3embree3
/usr/share/man/man3/rtcIntersect1.3embree3
/usr/share/man/man3/rtcIntersect1M.3embree3
/usr/share/man/man3/rtcIntersect1Mp.3embree3
/usr/share/man/man3/rtcIntersect4.3embree3
/usr/share/man/man3/rtcIntersectNM.3embree3
/usr/share/man/man3/rtcIntersectNp.3embree3
/usr/share/man/man3/rtcJoinCommitScene.3embree3
/usr/share/man/man3/rtcNewBVH.3embree3
/usr/share/man/man3/rtcNewBuffer.3embree3
/usr/share/man/man3/rtcNewDevice.3embree3
/usr/share/man/man3/rtcNewGeometry.3embree3
/usr/share/man/man3/rtcNewScene.3embree3
/usr/share/man/man3/rtcNewSharedBuffer.3embree3
/usr/share/man/man3/rtcOccluded1.3embree3
/usr/share/man/man3/rtcOccluded1M.3embree3
/usr/share/man/man3/rtcOccluded1Mp.3embree3
/usr/share/man/man3/rtcOccluded4.3embree3
/usr/share/man/man3/rtcOccludedNM.3embree3
/usr/share/man/man3/rtcOccludedNp.3embree3
/usr/share/man/man3/rtcPointQuery.3embree3
/usr/share/man/man3/rtcPointQuery4.3embree3
/usr/share/man/man3/rtcReleaseBVH.3embree3
/usr/share/man/man3/rtcReleaseBuffer.3embree3
/usr/share/man/man3/rtcReleaseDevice.3embree3
/usr/share/man/man3/rtcReleaseGeometry.3embree3
/usr/share/man/man3/rtcReleaseScene.3embree3
/usr/share/man/man3/rtcRetainBVH.3embree3
/usr/share/man/man3/rtcRetainBuffer.3embree3
/usr/share/man/man3/rtcRetainDevice.3embree3
/usr/share/man/man3/rtcRetainGeometry.3embree3
/usr/share/man/man3/rtcRetainScene.3embree3
/usr/share/man/man3/rtcSetDeviceErrorFunction.3embree3
/usr/share/man/man3/rtcSetDeviceMemoryMonitorFunction.3embree3
/usr/share/man/man3/rtcSetGeometryBoundsFunction.3embree3
/usr/share/man/man3/rtcSetGeometryBuffer.3embree3
/usr/share/man/man3/rtcSetGeometryBuildQuality.3embree3
/usr/share/man/man3/rtcSetGeometryDisplacementFunction.3embree3
/usr/share/man/man3/rtcSetGeometryInstancedScene.3embree3
/usr/share/man/man3/rtcSetGeometryIntersectFilterFunction.3embree3
/usr/share/man/man3/rtcSetGeometryIntersectFunction.3embree3
/usr/share/man/man3/rtcSetGeometryMask.3embree3
/usr/share/man/man3/rtcSetGeometryMaxRadiusScale.3embree3
/usr/share/man/man3/rtcSetGeometryOccludedFilterFunction.3embree3
/usr/share/man/man3/rtcSetGeometryOccludedFunction.3embree3
/usr/share/man/man3/rtcSetGeometryPointQueryFunction.3embree3
/usr/share/man/man3/rtcSetGeometrySubdivisionMode.3embree3
/usr/share/man/man3/rtcSetGeometryTessellationRate.3embree3
/usr/share/man/man3/rtcSetGeometryTimeRange.3embree3
/usr/share/man/man3/rtcSetGeometryTimeStepCount.3embree3
/usr/share/man/man3/rtcSetGeometryTopologyCount.3embree3
/usr/share/man/man3/rtcSetGeometryTransform.3embree3
/usr/share/man/man3/rtcSetGeometryTransformQuaternion.3embree3
/usr/share/man/man3/rtcSetGeometryUserData.3embree3
/usr/share/man/man3/rtcSetGeometryUserPrimitiveCount.3embree3
/usr/share/man/man3/rtcSetGeometryVertexAttributeCount.3embree3
/usr/share/man/man3/rtcSetGeometryVertexAttributeTopology.3embree3
/usr/share/man/man3/rtcSetNewGeometryBuffer.3embree3
/usr/share/man/man3/rtcSetSceneBuildQuality.3embree3
/usr/share/man/man3/rtcSetSceneFlags.3embree3
/usr/share/man/man3/rtcSetSceneProgressMonitorFunction.3embree3
/usr/share/man/man3/rtcSetSharedGeometryBuffer.3embree3
/usr/share/man/man3/rtcUpdateGeometryBuffer.3embree3

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/embree3/CHANGELOG.md
/usr/share/doc/embree3/LICENSE.txt
/usr/share/doc/embree3/README.md
/usr/share/doc/embree3/readme.pdf
/usr/share/doc/embree3/third-party-programs-TBB.txt
/usr/share/doc/embree3/third-party-programs.txt

%files extras
%defattr(-,root,root,-)
/usr/libexec/embree3/buildbench
/usr/libexec/embree3/bvh_access
/usr/libexec/embree3/bvh_builder
/usr/libexec/embree3/convert
/usr/libexec/embree3/curve_geometry
/usr/libexec/embree3/displacement_geometry
/usr/libexec/embree3/dynamic_scene
/usr/libexec/embree3/grid_geometry
/usr/libexec/embree3/hair_geometry
/usr/libexec/embree3/instanced_geometry
/usr/libexec/embree3/interpolation
/usr/libexec/embree3/intersection_filter
/usr/libexec/embree3/lazy_geometry
/usr/libexec/embree3/models/cornell_box.ecs
/usr/libexec/embree3/models/cornell_box.mtl
/usr/libexec/embree3/models/cornell_box.obj
/usr/libexec/embree3/models/cornell_box.xml
/usr/libexec/embree3/models/cornell_box.xml.bin
/usr/libexec/embree3/models/cornell_box_mblur.xml
/usr/libexec/embree3/models/cornell_box_mblur.xml.bin
/usr/libexec/embree3/models/curve0.xml
/usr/libexec/embree3/models/curve1.xml
/usr/libexec/embree3/models/cylinder.ecs
/usr/libexec/embree3/models/cylinder.xml
/usr/libexec/embree3/models/hair0.ecs
/usr/libexec/embree3/models/hair0.xml
/usr/libexec/embree3/models/hair1.xml
/usr/libexec/embree3/models/linesegments.ecs
/usr/libexec/embree3/models/linesegments.xml
/usr/libexec/embree3/models/mblur_time_range_curve.xml
/usr/libexec/embree3/models/mblur_time_range_grid.xml
/usr/libexec/embree3/models/mblur_time_range_line.xml
/usr/libexec/embree3/models/mblur_time_range_quad.xml
/usr/libexec/embree3/models/mblur_time_range_triangle.xml
/usr/libexec/embree3/models/oriented_curve0.xml
/usr/libexec/embree3/models/oriented_curve1.xml
/usr/libexec/embree3/models/oriented_curves.xml
/usr/libexec/embree3/models/subdiv0.ecs
/usr/libexec/embree3/models/subdiv0.xml
/usr/libexec/embree3/models/subdiv1.ecs
/usr/libexec/embree3/models/subdiv1.xml
/usr/libexec/embree3/models/subdiv3.ecs
/usr/libexec/embree3/models/subdiv3.xml
/usr/libexec/embree3/models/subdiv4.ecs
/usr/libexec/embree3/models/subdiv4.xml
/usr/libexec/embree3/models/subdiv5.ecs
/usr/libexec/embree3/models/subdiv5.xml
/usr/libexec/embree3/models/subdiv6.ecs
/usr/libexec/embree3/models/subdiv6.xml
/usr/libexec/embree3/models/subdiv7.ecs
/usr/libexec/embree3/models/subdiv7.xml
/usr/libexec/embree3/models/subdiv8.ecs
/usr/libexec/embree3/models/subdiv8.xml
/usr/libexec/embree3/models/subdiv9.ecs
/usr/libexec/embree3/models/subdiv9.xml
/usr/libexec/embree3/models/subdiv_no_boundary.ecs
/usr/libexec/embree3/models/subdiv_no_boundary.xml
/usr/libexec/embree3/models/subdiv_pin_all.ecs
/usr/libexec/embree3/models/subdiv_pin_all.xml
/usr/libexec/embree3/models/subdiv_pin_boundary.ecs
/usr/libexec/embree3/models/subdiv_pin_boundary.xml
/usr/libexec/embree3/models/subdiv_pin_corners.ecs
/usr/libexec/embree3/models/subdiv_pin_corners.xml
/usr/libexec/embree3/models/subdiv_smooth_boundary.ecs
/usr/libexec/embree3/models/subdiv_smooth_boundary.xml
/usr/libexec/embree3/motion_blur_geometry
/usr/libexec/embree3/pathtracer
/usr/libexec/embree3/point_geometry
/usr/libexec/embree3/subdivision_geometry
/usr/libexec/embree3/triangle_geometry
/usr/libexec/embree3/user_geometry
/usr/libexec/embree3/verify
/usr/libexec/embree3/viewer
/usr/libexec/embree3/viewer_anim
/usr/libexec/embree3/viewer_stream

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libembree3.so.3
/usr/lib64/haswell/avx512_1/libembree3.so.3.12.0
/usr/lib64/haswell/libembree3.so.3
/usr/lib64/haswell/libembree3.so.3.12.0
/usr/lib64/libembree3.so.3
/usr/lib64/libembree3.so.3.12.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/embree3/closest_point
/usr/libexec/embree3/collide
/usr/libexec/embree3/embree_tests
/usr/libexec/embree3/minimal
/usr/libexec/embree3/models/curve_flat.ecs
/usr/libexec/embree3/models/curve_flat.xml
/usr/libexec/embree3/models/curve_geometry.xml
/usr/libexec/embree3/models/curve_oriented.ecs
/usr/libexec/embree3/models/curve_oriented.xml
/usr/libexec/embree3/models/curve_round.ecs
/usr/libexec/embree3/models/curve_round.xml
/usr/libexec/embree3/models/furBall_A.bin
/usr/libexec/embree3/models/furBall_A.ecs
/usr/libexec/embree3/models/furBall_A.xml
/usr/libexec/embree3/models/hair1.ecs
/usr/libexec/embree3/models/oriented_bspline_curve_twisted.xml
/usr/libexec/embree3/models/oriented_hermite_curve_twisted.xml
/usr/libexec/embree3/models/points.ecs
/usr/libexec/embree3/models/points.xml
/usr/libexec/embree3/models/round_line_segments_0.ecs
/usr/libexec/embree3/models/round_line_segments_0.xml
/usr/libexec/embree3/models/round_line_segments_1.ecs
/usr/libexec/embree3/models/round_line_segments_1.xml
/usr/libexec/embree3/models/round_line_segments_2.ecs
/usr/libexec/embree3/models/round_line_segments_2.xml
/usr/libexec/embree3/models/round_line_segments_3.ecs
/usr/libexec/embree3/models/round_line_segments_3.xml
/usr/libexec/embree3/models/round_line_segments_4.ecs
/usr/libexec/embree3/models/round_line_segments_4.xml
/usr/libexec/embree3/models/round_line_segments_5.ecs
/usr/libexec/embree3/models/round_line_segments_5.xml
/usr/libexec/embree3/models/round_line_segments_6.ecs
/usr/libexec/embree3/models/round_line_segments_6.xml
/usr/libexec/embree3/multiscene_geometry
/usr/libexec/embree3/next_hit
/usr/libexec/embree3/quaternion_motion_blur
/usr/libexec/embree3/voronoi

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/embree/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/embree/35c378e9a2394a10656c4f7075323670e5bfd5f5
/usr/share/package-licenses/embree/d3c41d58a2a6a19465e61e6710203244faec7db2
