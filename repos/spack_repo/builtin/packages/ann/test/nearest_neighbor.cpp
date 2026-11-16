// Copyright Spack Project Developers. See COPYRIGHT file for details.
//
// SPDX-License-Identifier: (Apache-2.0 OR MIT)

#include <ANN/ANN.h>
#include <cmath>
#include <iostream>

int main() {
    ANNpointArray points = annAllocPts(3, 2);
    for (int i = 0; i < 3; ++i) {
        points[i][0] = i == 2 ? 3.0 : double(i);
        points[i][1] = points[i][0];
    }
    ANNpoint query = annAllocPt(2);
    query[0] = query[1] = 1.1;
    bool ok;
    {
        ANNkd_tree tree(points, 3, 2);
        ANNidx indices[2];
        ANNdist distances[2];
        tree.annkSearch(query, 2, indices, distances, 0.0);
        ok = indices[0] == 1 && indices[1] == 0 &&
             std::abs(distances[0] - 0.02) < 1e-12 &&
             std::abs(distances[1] - 2.42) < 1e-12;
    }
    annDeallocPt(query);
    annDeallocPts(points);
    annClose();
    if (!ok) return 1;
    std::cout << "PASS ANN: nearest indices [1,0], squared distances [0.02,2.42]" << std::endl;
}
